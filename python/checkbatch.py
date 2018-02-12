import subprocess as sb
import sys, re, os

def check_jobs(jnames) :
    
    if isinstance(jnames,str) : jnames = [jnames]
    out = sb.check_output("bjobs -o 'JOBID:10 STAT:5 SUBMIT_TIME:13 JOB_NAME:40'", shell=True).decode('utf-8')
    out = '\n'.join(str(out).split('\\n'))
    
    d = {'RUN' : 0, 'PEND' : 0}
    for jname in jnames :
        for l in out.split('\n')[1:] :
            if jname not in l and len(re.findall(jname,l)) <= 0 : continue

            toks = l.split()
            status = toks[1]         
            if status in d.keys() : d[status] += 1
            else : d[status] = 1
    
    return d

def is_job_done(name) :

    d = check_jobs(name)
    if d['PEND'] == 0 and d['RUN'] == 0 :
        return True
    return False

def wait_batch(jobs,callback=None) :
    
    if isinstance(jobs,str) : jobs = [jobs]    
    from time import sleep
    done = False
    while not done :
        done = True
        allstatus = {}
        for j in jobs :
            status = check_jobs(j)
            allstatus = { k: status.get(k, 0) + allstatus.get(k, 0) for k in set(status) | set(allstatus) }
        
        if allstatus['PEND'] > 0 or allstatus['RUN'] > 0 : 
            done = False
            print(allstatus)
        sleep(1)

    if callback is not None : callback();


if __name__ == '__main__' :

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-j","--jname",default = None)
    parser.add_argument("-w","--wait",action="store_true")
    args = parser.parse_args()

    if args.wait : 
        wait_batch(args.jname)
    else :
        d = check_jobs(args.jname)
        print (d)
        print ("Done: ", is_job_done(args.jname))


