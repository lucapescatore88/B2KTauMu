import os, sys, glob

import warnings
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )

if os.getenv('B2KTAUMUROOT') is None :
    print ("Attention, you did not setup. Run 'source setup.sh' before doing anything")
    sys.exit()

import ROOT
import cuts
import getdata as data
import utils

repo = os.getenv('B2KTAUMUROOT')
from pyutils.LHCb.LHCbStyle import set_lhcbStyle
set_lhcbStyle()

from locations import loc, dataids

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

