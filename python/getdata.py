from ROOT import *
from glob import glob
from B2KTauMuEnv import *
import subprocess

def inspect(nametag) :

    if nametag not in dataids.keys() :
        print "No nametag", nametag
        return

    listoffiles = []
    for cid in dataids[nametag][1] :
        jdir = "{root}/{jid}".format(root=dataids[nametag][0],jid=cid)
        pattern = jdir+"/*/DVNtuple.root"

        print "Fetching data from", pattern
        if 'lxplus' in os.getenv('HOSTNAME'): listoffiles += glob.glob(pattern)
        else:
            try:
                cmd = 'xrdfs root://eoslhcb.cern.ch/ ls {0}/'.format(jdir)
                print cmd
                lsout = subprocess.check_output(cmd,shell=True)
                lines = lsout.split()
                listoffiles += [line+"/DVNtuple.root" for line in lines]
            except:
                print "No directory", jdir, "available or no eos access"
                continue
    
    if not len(listoffiles) : 
        print "Sorry no files found"
        return

    f = TFile.Open(listoffiles[0])
    myiter = TFileIter(f)
    obj    = myiter

    trees = []
    for i in range(myiter.TotalKeys()) :
        if '0x(nil)' in obj.__str__() : continue
        trees.append(obj.GetName())
        obj = myiter.Next()

    return {'files' : listoffiles, 'trees' : trees}


def get_data(nametag,treetag=None,maxfiles=1e4,check=False) :
    
    d = inspect(nametag)
    trees = d['trees']
    if treetag is not None :
        if treetag in trees : trees = [treetag]
        else : print "Requested tree not available, retrieving all available trees"

    out = {}
    for t in trees : 
        if 'Luminosity' in t : out[t] = TChain(t+'/LumiTuple')
        else : out[t] = TChain(t+'/DecayTree')
    
    for fi,f in enumerate(d['files']) :
        if fi >= maxfiles : break
        
        cf = TFile.Open(f)
        
        for t in trees :

            if check :
                ct = cf.Get(t)
                if '0x(nil)' in ct.GetName() :
                    print "No tree", t, "found in file", f
                    continue
            
            out[t].AddFile('root://eoslhcb.cern.ch/'+f)

    print "Data retrieved"
    return out

