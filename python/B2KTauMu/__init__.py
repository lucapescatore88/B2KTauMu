import os, sys, glob

import warnings
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )

if os.getenv('B2KTAUMUROOT') is None :
    print "Attention, you did not setup. Run 'source setup.sh' before doing anything"
    sys.exit()

import ROOT
import cuts
import getdata as data

repo = os.getenv('B2KTAUMUROOT')
ROOT.gROOT.ProcessLine('.x '+repo+'/LHCb/lhcbStyle.C')

#from utils.cut_converter import CutConverter
#cuts = CutConverter(os.getenv('B2KTAUMUROOT')+'/cpp/include/Lb2LemuAnaCuts.hpp')

################## Location in repository or on EOS

class loc : pass
loc.ROOT       = repo
loc.PYTHON     = loc.ROOT+'/python/'
loc.PLOTS      = loc.ROOT+'/plots/'
loc.LHCB       = loc.ROOT+'/LHCb/'
loc.TMPS       = loc.ROOT+'/tables/templates/'
loc.TABS       = loc.ROOT+'/tables/'
loc.TUPLE      = os.getenv('LBTUPLELOC')
loc.LUCAJOBS   = os.getenv('LBLUCAJOBLOC')
loc.LUCAANAEOS = os.getenv('LUCAANAEOSLOC')

### Raw data locations

dataids = { 

        'CL11'        :(loc.LUCAJOBS, [602,603]),
        'CL12'        :(loc.LUCAJOBS, [604,605]),
        'CL15'        :(loc.LUCAJOBS, [610,607]),
        'CL16'        :(loc.LUCAJOBS, [608,609]),

        'CL11_BH'        :(loc.LUCAJOBS, [642,643]),
        'CL12_BH'        :(loc.LUCAJOBS, [644,645]),
        'CL15_BH'        :(loc.LUCAJOBS, [646,647]),
        'CL16_BH'        :(loc.LUCAJOBS, [648,649]),

        #'MCLc2pmm'     : [510,511], ##
          }


################# Values database and outputfiles

import pickle

if not os.path.exists(loc.LHCB+"db.pkl") :
    pickle.dump({},open(loc.LHCB+"db.pkl","w"))

db = pickle.load(open(loc.LHCB+"db.pkl"))

def dumpDB() :
    pickle.dump(db,open(loc.LHCB+"db.pkl","w"))


from pyutils.editing.formatter import PartialFormatter as Formatter

class Outfiles :

    def __init__(self) :
        
        if not os.path.exists(loc.LHCB+"outfiles_list.txt") :
            f = open(loc.LHCB+"outfiles_list.txt","w")
            f.close()

        lines = open(loc.LHCB+"outfiles_list.txt").readlines()
        self.files = {}
        for l in lines :
            toks = l.split()
            self.files[toks[0]] = toks[1]

    def writeline(self,name,text,clear=False) :

        self.write(name,text+"\n",clear)

    def write(self,name,text,clear=False) :

        if clear : f = open(self.files[name],"w")
        else : f = open(self.files[name],"a")
        f.write(text)
        f.close()

    def fill_template(self,name,template,dic = db) :
        
        tmp = open(loc.TMPS+template)
        
        fmt = Formatter()
        out = fmt.format(tmp.read(),**dic)

        self.write(name,out,clear=True)

    def create(self,name,filename=None, extension=".txt") :

        if filename == None : filename = name
        if "." not in filename : filename += extension

        path = loc.TABS+filename
        self.files[name] = path

        f = open(loc.LHCB+"outfiles_list.txt","w")
        for n,p in self.files.iteritems() :
            f.write(n+" "+p)

outfiles = Outfiles()

