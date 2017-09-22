from Gaudi.Configuration       import *
from GaudiKernel.SystemOfUnits import *

#####################################################################
#
# Define template tuple
#
######################################################################

from Configurables import DecayTreeTuple
TupTmp          = DecayTreeTuple()
######################################################################
from Configurables import TupleToolDecay
TupTmp.addTool( TupleToolDecay, name = "B" )
TupTmp.addTool( TupleToolDecay, name = "H" )
TupTmp.addTool( TupleToolDecay, name = "K" )
TupTmp.addTool( TupleToolDecay, name = "mu" )
TupTmp.addTool( TupleToolDecay, name = "tau" )
TupTmp.addTool( TupleToolDecay, name = "pi1" )
TupTmp.addTool( TupleToolDecay, name = "pi2" )
TupTmp.addTool( TupleToolDecay, name = "pi3" )

######################################################################
TupTmp.ToolList += [
    "TupleToolEventInfo",
    "TupleToolANNPID",
    "TupleToolAngles",
    #"TupleToolBremInfo",
    "TupleToolGeometry",
    "TupleToolKinematic",
    "TupleToolPid",
    "TupleToolPrimaries",
    "TupleToolPropertime",
    "TupleToolRecoStats",
    "TupleToolTrackInfo",
    "TupleToolDira"
    ]

from Configurables import TupleToolTrackInfo
TupTmp.addTool(TupleToolTrackInfo, name="TupleToolTrackInfo")
TupTmp.ToolList += [ "TupleToolTrackInfo"]
TupTmp.TupleToolTrackInfo.Verbose = True

######################################################################
# Include TupleToolL0Calo for correction of ET cut in 2016 samples + possibility to bin in CaloRegions
#from Configurables import TupleToolL0Calo 

from Configurables import TupleToolTISTOS
for particle in [TupTmp.B,TupTmp.tau,TupTmp.H,TupTmp.K,TupTmp.pi1,TupTmp.pi2,TupTmp.pi3,TupTmp.mu]:
    particle.addTool( TupleToolTISTOS, name = "L0TISTOS" )
    particle.ToolList += [ "TupleToolTISTOS/L0TISTOS" ]

    particle.L0TISTOS.TriggerList = [
	"L0ElectronDecision",
	"L0HadronDecision",
	"L0MuonDecision",
	"L0DiMuonDecision",
	"L0PhotonDecision",
    "L0ElectronHighDecision"
    ]
    particle.L0TISTOS.Verbose = True

TupTmp.B.addTool( TupleToolTISTOS, name = "HltTISTOS" )
TupTmp.B.ToolList += [ "TupleToolTISTOS/HltTISTOS" ]

TupTmp.B.HltTISTOS.TriggerList = [
	"Hlt1TrackAllL0Decision",
	"Hlt1TrackAllL0TightDecision",
	"Hlt1TrackMuonDecision",
    "Hlt1MuTrackDecision",
	"Hlt1TrackPhotonDecision",
	"Hlt1TrackMVADecision",
	"Hlt1TrackMVALooseDecision",
	"Hlt1TrackMuonMVADecision",
	"Hlt1TwoTrackMVALooseDecision",
	"Hlt1TwoTrackMVADecision",
	"Hlt1SingleMuonHighPTDecision",
	"Hlt1SingleMuonDecision",
	"Hlt1DiMuonHighMassDecision",

    "Hlt2SingleMuonDecision",
	"Hlt2DiMuonDetachedDecision",
    "Hlt2SingleElectronTFHighPtDecision",
	"Hlt2SingleElectronTFLowPtDecision",

	"Hlt2Topo2BodyDecision",
	"Hlt2Topo3BodyDecision",
	"Hlt2Topo4BodyDecision",
	"Hlt2TopoE2BodyDecision",
	"Hlt2TopoE3BodyDecision",
	"Hlt2TopoE4BodyDecision",
	"Hlt2TopoEE2BodyDecision",
	"Hlt2TopoEE3BodyDecision",
	"Hlt2TopoEE4BodyDecision",
	"Hlt2TopoMu2BodyDecision",
	"Hlt2TopoMu3BodyDecision",
	"Hlt2TopoMu4BodyDecision",
	"Hlt2TopoMuE2BodyDecision",
	"Hlt2TopoMuE3BodyDecision",
	"Hlt2TopoMuE4BodyDecision"

	"Hlt2Topo2BodyBBDTDecision",
	"Hlt2Topo3BodyBBDTDecision",
	"Hlt2Topo4BodyBBDTDecision",
	"Hlt2TopoE2BodyBBDTDecision",
	"Hlt2TopoE3BodyBBDTDecision",
	"Hlt2TopoE4BodyBBDTDecision",
	"Hlt2TopoMu2BodyBBDTDecision",
	"Hlt2TopoMu3BodyBBDTDecision",
	"Hlt2TopoMu4BodyBBDTDecision",
	]
TupTmp.B.HltTISTOS.Verbose = True

from Configurables import TupleToolDecayTreeFitter
TupTmp.B.addTool( TupleToolDecayTreeFitter, name = "DTF" )
TupTmp.B.ToolList += [ "TupleToolDecayTreeFitter/DTF" ]
TupTmp.B.addTool( TupTmp.B.DTF.clone( "DTF_PV",
                                      Verbose = True,
                                      constrainToOriginVertex = True ) )
TupTmp.B.ToolList += [ "TupleToolDecayTreeFitter/DTF_PV" ]
TupTmp.B.addTool( TupTmp.B.DTF.clone( "DTF_Tau_PV",
                                      Verbose = True,
                                      constrainToOriginVertex = True,
                                      daughtersToConstrain = [ "tau+" ] ) )
TupTmp.B.ToolList += [ "TupleToolDecayTreeFitter/DTF_Tau_PV" ]
TupTmp.B.addTool( TupTmp.B.DTF.clone( "DTF_B_PV",
                                      Verbose = True,
                                      constrainToOriginVertex = True,
                                      daughtersToConstrain = [ "B+" ] ) )
TupTmp.B.ToolList += [ "TupleToolDecayTreeFitter/DTF_B_PV" ]

# Adding loki functors

from Configurables import LoKi__Hybrid__TupleTool
lokiCommon = LoKi_MIPCHI2 = LoKi__Hybrid__TupleTool("lokiCommon")
TupTmp.ToolList += ["LoKi::Hybrid::TupleTool/lokiCommon"]
TupTmp.addTool(lokiCommon)
TupTmp.lokiCommon.Variables['MINIP']     = "MIPDV(PRIMARY)"
TupTmp.lokiCommon.Variables['MINIPCHI2'] = "MIPCHI2DV(PRIMARY)"

TupTmp.B.InheritTools   = True
TupTmp.tau.InheritTools = True

lokiB   = LoKi__Hybrid__TupleTool("lokiB")
TupTmp.B.ToolList += ["LoKi::Hybrid::TupleTool/lokiB"]
lokitau = LoKi__Hybrid__TupleTool("lokitau")
TupTmp.tau.ToolList += ["LoKi::Hybrid::TupleTool/lokitau"]

lokiB.Variables = {
           "DOCAtauRest"  : "DOCA(1,2)",
           #"DOCAtaumu" : "DOCA(CHILD(CHILD(1),1),2)",
           #"DOCAKmu"   : "DOCA(1,3)",
           "DOCAMAX"   : "DOCAMAX",
           "BPVVDCHI2" : "BPVVDCHI2",
           "BPVVDRHO"  : "BPVVDRHO",
           "BPVVDZ"    : "BPVVDZ"
           #, "Mtaumu"    : "M23" 
           }

lokitau.Variables = {
           "DOCA12"    : "DOCA(1,2)",
           "DOCA23"    : "DOCA(2,3)",
           "DOCA13"    : "DOCA(1,3)",
           "DOCAMAX"   : "DOCAMAX",
           "BPVVDCHI2" : "BPVVDCHI2",
           "BPVVDRHO"  : "BPVVDRHO",
           "BPVVDZ"    : "BPVVDZ",
           "M12"       : "M12",
           "M23"       : "M23",
           "M13"       : "M13" }

TupTmp.B.addTool(lokiB)
TupTmp.tau.addTool(lokitau)

#from Configurables import TupleToolDocas
#TupTmp.B.addTool( TupleToolDocas )
#TupTmp.B.ToolList += [ "TupleToolDocas" ]
#docas = TupTmp.B.addTupleTool('TupleToolDocas')
#docas.Name       = [ "Kmu_OS", "Kmu_SS", "mutau_mp", "mutau_pm", "Ktau_SS", "Ktau_OS" ]
#docas.Location1  = [ "[B+ -> (K*(1410)0 -> ^K+ mu-) (tau+ -> pi+ pi- pi+)]CC",
#                     "[B+ -> (Delta(1600)++ -> ^K+ mu+) (tau- -> pi- pi+ pi-)]CC",
#                     "[B+ -> (K*(1410)0 -> K+ ^mu-) (tau+ -> pi+ pi- pi+)]CC",
#                     "[B+ -> (Delta(1600)++ -> K+ ^mu+) (tau- -> pi- pi+ pi-)]CC",
#                     "[B+ -> (K*(1410)0 -> ^K+ mu-) (tau+ -> pi+ pi- pi+)]CC",
#                     "[B+ -> (Delta(1600)++ -> ^K+ mu+) (tau- -> pi- pi+ pi-)]CC"
#                    ]
#docas.Location2  = [ "[B+ -> (K*(1410)0 -> K+ ^mu-) (tau+ -> pi+ pi- pi+)]CC",
#                     "[B+ -> (Delta(1600)++ -> K+ ^mu+) (tau- -> pi- pi+ pi-)]CC",
#                     "[B+ -> (K*(1410)0 -> K+ mu-) ^(tau+ -> pi+ pi- pi+)]CC",
#                     "[B+ -> (Delta(1600)++ -> K+ mu+) ^(tau- -> pi- pi+ pi-)]CC",
#                     "[B+ -> (K*(1410)0 -> K+ mu-) ^(tau+ -> pi+ pi- pi+)]CC",
#                     "[B+ -> (Delta(1600)++ -> K+ mu+) ^(tau- -> pi- pi+ pi-)]CC"
#                     ]
   

#######################################################################

from Configurables import TupleToolSubMass
TupTmp.B.addTool( TupleToolSubMass )
TupTmp.B.ToolList += [ "TupleToolSubMass" ]
TupTmp.B.TupleToolSubMass.EndTreePIDs = [22]

TupTmp.B.TupleToolSubMass.Substitution       += [ "K+ => pi+" ]
TupTmp.B.TupleToolSubMass.Substitution       += [ "pi- => p~-" ]
TupTmp.B.TupleToolSubMass.Substitution       += [ "pi- => K-" ]
TupTmp.B.TupleToolSubMass.Substitution       += [ "pi- => mu-" ]
TupTmp.B.TupleToolSubMass.Substitution       += [ "pi- => e-" ]

#TupTmp.B.TupleToolSubMass.DoubleSubstitution += [ "p+/pi- => pi+/p~-" ]

########################################### MC truth info for simulated samples

TupTmpMC = TupTmp.clone("DecayTreeTupleForMC") 
 
from Configurables import TupleToolMCTruth 

TupTmpMC.addTool( TupleToolMCTruth ) 
TupTmpMC.ToolList += [ "TupleToolMCTruth" ] 
TupTmpMC.TupleToolMCTruth.ToolList += [ "MCTupleToolHierarchy" ] 
TupTmpMC.TupleToolMCTruth.ToolList += [ "MCTupleToolKinematic" ] 
  
TupTmpMC.B.addTool( TupleToolMCTruth ) 
TupTmpMC.B.ToolList += [ "TupleToolMCTruth" ] 

from Configurables import TupleToolMCBackgroundInfo
TupTmpMC.B.ToolList += [ "TupleToolMCBackgroundInfo" ]


