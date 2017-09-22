import os, sys

root = os.getenv("B2KTAUMUROOT")
if root is not None : 
    sys.path.append(root+"/Options" )
sys.path.append(os.getcwd())

from DV_Routines import set_branches
from DV_RelatedInfo import getLoKiTool
from DV_DecayTuple import TupTmp, TupTmpMC
from DV_Config import ConfigDaVinci
from DB import decays_db

from Gaudi.Configuration       import *
from GaudiKernel.SystemOfUnits import *
from Configurables import TupleToolDecay
from Configurables import DeterministicPrescaler

######################################################################


#from DV_Routines import ReStrip
#lines_to_restrip = [ 
#        'StrippingBu2LLK_meLine',
#        'StrippingBu2LLK_meSSLine',
#        'StrippingBu2LLK_eeLine',
#        'StrippingBu2LLK_mmLine'
#        ]
#
#restrip, restripSq = ReStrip(lines_to_restrip,["Bu2LLK"],['Leptonic'])

#####################################################################
#
# Define DecayTreeTuple tuple
#
######################################################################

#branches = ["B","H","tau","pi1","pi2","pi3","mu"]
branchesX = ["B","H","K","mu","tau","pi1","pi2","pi3"]
#branchesX = ["B","K","mu","tau","pi1","pi2","pi3"]

algs = []

def setalgs(isMC=False,decay='LEPTONIC') :

    global TupTmp, TupTmpMC
    if isMC : TupTmp = TupTmpMC
        
    linePi = "LFVB2PiTauMuLine"
    lineK  = "LFVB2KTauMuLine"
    lineXK = "B2XTauMu_K_3pi_looseLine"
    
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

    #B2heMuTuple = TupTmp.clone("B2heMuTuple")
    #B2heMuTuple.Inputs   = [ 'Phys/LFVB2heMuLine/Particles' ]
    #B2heMuTuple.Decay    = "[B+ -> K+ e+ mu-]CC"
    #B2KTauMuSSTuple.Branches = set_branches(B2KTauMuSSTuple.Decay,branches)
    
    XB2KTauMuLine_ppm = TupTmp.clone("B2KMuTau_ppmTuple")
    XB2KTauMuLine_ppm.Inputs   = [ inputname.format(lineXK) ]
    XB2KTauMuLine_ppm.Decay    = "[B+ -> ^(Delta(1600)++ -> ^K+ ^mu+) ^(tau- -> ^pi- ^pi+ ^pi-)]CC"
    XB2KTauMuLine_ppm.Branches = set_branches(XB2KTauMuLine_ppm.Decay,branchesX)
    LoKi_Tool1 = getLoKiTool("1",lineXK,isMC,branch=XB2KTauMuLine_ppm.B)
    
    XB2KTauMuLine_pmp = TupTmp.clone("B2KMuTau_pmpTuple")
    XB2KTauMuLine_pmp.Inputs   = [ inputname.format(lineXK) ]
    XB2KTauMuLine_pmp.Decay    = "[B+ -> ^(K*(1410)0 -> ^K+ ^mu-) ^(tau+ -> ^pi+ ^pi- ^pi+)]CC"
    XB2KTauMuLine_pmp.Branches = set_branches(XB2KTauMuLine_pmp.Decay,branchesX)
    LoKi_Tool2 = getLoKiTool("2",lineXK,isMC,branch=XB2KTauMuLine_pmp.B)
    
    XB2KTauMuLine_SS = TupTmp.clone("B2KMuTau_SSTuple")
    XB2KTauMuLine_SS.Inputs   = [ inputname.format(lineXK) ]
    XB2KTauMuLine_SS.Decay    = "[B+ -> ^(K*(1410)0 -> ^K- ^mu+) ^(tau+ -> ^pi+ ^pi- ^pi+)]CC"
    XB2KTauMuLine_SS.Branches = set_branches(XB2KTauMuLine_SS.Decay,branchesX)
    LoKi_Tool3 = getLoKiTool("3",lineXK,isMC,branch=XB2KTauMuLine_SS.B)

    global algs
    algs = [ XB2KTauMuLine_ppm, XB2KTauMuLine_pmp, XB2KTauMuLine_SS, LFVB2PiTauMuLine, LFVB2KTauMuLine ]

    if not isMC : return
    
    print "Adding MCDecayTreeTuple"

    from DV_MCDecayTuple import MCTupTmp

    MCTuple          = MCTupTmp.clone("MCTuple")
    MCTuple.Decay    = '({0})'.format(decays_db[decay.replace('Filtered_', '')]['descriptor'])
    MCTuple.Branches = set_branches(MCTuple.Decay,branchesX)
    algs += [ MCTuple ]
     
