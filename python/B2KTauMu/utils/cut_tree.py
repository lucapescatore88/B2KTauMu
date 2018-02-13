import ROOT as r
from B2KTauMu import cuts, loc
import sys, os, argparse
    
def cut(dtype,nick,nevt,tree,files,odir,test): 

    outfname = odir+"/%s_%s.root" % (dtype,nick)
    if test : outfname = odir+"/test.root"
    
    print "Writing to", outfname
    outf = r.TFile(outfname,"RECREATE")
    
    trees = tree
    if "[" in trees :
        trees = trees.replace("[","").replace("]","")
        trees = trees.split(',')
    
    for tname in trees :
    
        print "Processing ", tname
        tree = r.TChain(tname)
        for f in files : tree.AddFile(f)
        
        cut = r.TCut("")      
        cut.Print()
        
        try :
            if nevt == -1 : nevt = tree.GetEntries()
            copy = tree.CopyTree(cut.GetTitle(),"",nevt)
            print "N selected events: %s / %s" % (copy.GetEntries(),tree.GetEntries())
            print "Selection efficiency: ", float(copy.GetEntries())/tree.GetEntries()
        
            copy.Write(tname.replace("/DecayTree","_CutTree"))
        except :
            continue
    
    outf.Close()
    
if __name__ == '__main__' :

    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--dtype',default='CL12')
    parser.add_argument('-e','--nevt',type=int,default=-1)
    parser.add_argument('-t','--tree',required=True)
    parser.add_argument('-f','--files',required=True,nargs='+')
    parser.add_argument('-o','--odir',default=loc.TMP)
    parser.add_argument('-n','--nick',default="")
    parser.add_argument('--test',action="store_true")
    opts = parser.parse_args()

    cut(opts.dtype,opts.nick,opts.nevt,opts.tree,opts.files,opts.odir,opts.test)

   
