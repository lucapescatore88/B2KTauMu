import os, sys

root = os.getenv("B2KTAUMUROOT")
if root is not None : 
    sys.path.append(root+"/Options" )
sys.path.append(os.getcwd())

from DV_Routines import set_branches
from DV_RelatedInfo import getLoKiTool
from DV_DecayTuple import TupTmp, TupTmpMC, TupTmpNorm
from DV_Config import ConfigDaVinci
from DB import decays_db

from Gaudi.Configuration       import *
from GaudiKernel.SystemOfUnits import *
from Configurables import TupleToolDecay
from Configurables import DeterministicPrescaler

#####################################################################
#
# Define DecayTreeTuple tuple
#
######################################################################

branches = ["B","H","K","mu","tau","pi1","pi2","pi3"]
branchesNorm = ["B","D0","K","pi","D","K1","K2","piD"]

algs = []

def setalgs(isMC=False,decay='LEPTONIC') :

    global TupTmp, TupTmpMC
    if isMC : TupTmp = TupTmpMC
        
    linePi  = "LFVB2PiTauMuLine"
    lineK   = "LFVB2KTauMuLine"
    lineXK  = "B2XTauMu_K_3pi_looseLine"
    lineDDs = "B2D0DBeauty2CharmLine" 
    
    #if decay.replace('Filtered_','') in ['Lb_Lee','Lb_Lemu','Lb_Lmm','Bd_Ksee','Bd_Ksmm']:
    #    branches_MC     = branchesRareMC
    #else: branches_MC     = branches

    if isMC: inputname = "AllStreams/Phys/{0}/Particles"
    else: inputname = "Phys/{0}/Particles"

    #LFVB2PiTauMuLine = TupTmp.clone("LFVB2PiTauMu")
    #LFVB2PiTauMuLine.Inputs   = [ inputname.format(linePi) ]
    #LFVB2PiTauMuLine.Decay    = "([B+ -> ^pi+ ^(tau+ -> ^pi+ ^pi- ^pi+) ^mu-]CC) || ([B+ -> ^pi+ ^(tau- -> ^pi- ^pi+ ^pi-) ^mu+ ]CC) || ([B+ -> ^pi- ^(tau+ -> ^pi+ ^pi- ^pi+) ^mu+]CC)"
    #LFVB2PiTauMuLine.Branches = set_branches(LFVB2PiTauMuLine.Decay,branches)

    #LoKi_ToolPi = getLoKiTool("K",linePi,isMC)
    #LFVB2PiTauMuLine.B.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_ToolPi"]
    #LFVB2PiTauMuLine.B.addTool(LoKi_ToolPi)

    #LFVB2KTauMuLine = TupTmp.clone("LFVB2KTauMu")
    #LFVB2KTauMuLine.Inputs   = [ inputname.format(lineK) ]
    #LFVB2KTauMuLine.Decay    = "([B+ -> ^K+ ^(tau+ -> ^pi+ ^pi- ^pi+) ^mu-]CC) || ([B+ -> ^K+ ^(tau- -> ^pi- ^pi+ ^pi-) ^mu+ ]CC) || ([B+ -> ^K- ^(tau+ -> ^pi+ ^pi- ^pi+) ^mu+]CC)"
    #LFVB2KTauMuLine.Branches = set_branches(LFVB2KTauMuLine.Decay,branches) 

    #LoKi_ToolK = getLoKiTool("K",lineK,isMC)
    #LFVB2KTauMuLine.B.ToolList += ["LoKi::Hybrid::TupleTool/LoKi_ToolK"]
    #LFVB2KTauMuLine.B.addTool(LoKi_ToolK)

    B2KTauMuLine_ppm = TupTmp.clone("B2KMuTau_ppmTuple")
    B2KTauMuLine_ppm.Inputs   = [ inputname.format(lineXK) ]
    B2KTauMuLine_ppm.Decay    = "[B+ -> ^(Delta(1600)++ -> ^K+ ^mu+) ^(tau- -> ^pi- ^pi+ ^pi-)]CC"
    B2KTauMuLine_ppm.Branches = set_branches(B2KTauMuLine_ppm.Decay,branches)
    LoKi_Tool1 = getLoKiTool("1",lineXK,isMC,branch=B2KTauMuLine_ppm.B)
    
    B2KTauMuLine_pmp = TupTmp.clone("B2KMuTau_pmpTuple")
    B2KTauMuLine_pmp.Inputs   = [ inputname.format(lineXK) ]
    B2KTauMuLine_pmp.Decay    = "[B+ -> ^(K*(1410)0 -> ^K+ ^mu-) ^(tau+ -> ^pi+ ^pi- ^pi+)]CC"
    B2KTauMuLine_pmp.Branches = set_branches(B2KTauMuLine_pmp.Decay,branches)
    LoKi_Tool2 = getLoKiTool("2",lineXK,isMC,branch=B2KTauMuLine_pmp.B)
    
    B2KTauMuLine_SS = TupTmp.clone("B2KMuTau_SSTuple")
    B2KTauMuLine_SS.Inputs   = [ inputname.format(lineXK) ]
    B2KTauMuLine_SS.Decay    = "[B+ -> ^(K*(1410)0 -> ^K- ^mu+) ^(tau+ -> ^pi+ ^pi- ^pi+)]CC"
    B2KTauMuLine_SS.Branches = set_branches(B2KTauMuLine_SS.Decay,branches)
    LoKi_Tool3 = getLoKiTool("3",lineXK,isMC,branch=B2KTauMuLine_SS.B)

    B2DDs = TupTmpNorm.clone("B2DDs_Kpi_Kpipi")
    B2DDs.Inputs   = [ inputname.format(lineDDs) ]
    B2DDs.Decay    = "[ B+ -> ^(D0 -> ^K- ^pi+) ^(D+ -> ^K+ ^K- ^pi+) ]CC"
    B2DDs.Branches = set_branches(B2DDs.Decay,branchesNorm)
    LoKi_Tool4 = getLoKiTool("4",lineDDs,isMC,branch=B2DDs.B)
 

    global algs
    algs = [ B2KTauMuLine_ppm, B2KTauMuLine_pmp, B2KTauMuLine_SS, B2DDs ]

    if not isMC : return
    
    print "Adding MCDecayTreeTuple"

    from DV_MCDecayTuple import MCTupTmp

    MCTuple          = MCTupTmp.clone("MCTuple")
    MCTuple.Decay    = '({0})'.format(decays_db[decay.replace('Filtered_', '')]['descriptor'])
    MCTuple.Branches = set_branches(MCTuple.Decay,branchesX)
    algs += [ MCTuple ]
    
