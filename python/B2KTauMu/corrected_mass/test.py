from pyutils.scripts.remotels import remotels
from B2KTauMu import *
import ROOT as r
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-d","--decay", default  = "MC12_Bu2KTauMu3pi")
parser.add_argument("-v","--verbose", action = "store_true")
parser.add_argument("-i","--inpt", default  = None)
args = parser.parse_args()

if args.inpt is None : args.inpt = dataids[args.decay][0]
locs = [ args.inpt+str(i) for i in dataids[args.decay][1] ]
datafiles = remotels(locs,levels=1,pattern=".root",backend="local")
if args.verbose : print datafiles

c = r.TCanvas()
data = r.TChain('B2KMuTau_pmpTuple/DecayTree')
dataSS = r.TChain('B2KMuTau_ppmTuple/DecayTree')
for df in datafiles :
    data.AddFile(df)
    dataSS.AddFile(df)

data.Draw("B_M")
c.Print(args.decay+"_M.pdf")
dataSS.Draw("B_M")
c.Print(args.decay+"_SS_M.pdf")

data.Draw("tau_M")
c.Print(args.decay+"_tauM.pdf")
dataSS.Draw("tau_M")
c.Print(args.decay+"_SS_tauM.pdf")






