#-- GAUDI jobOptions generated on Mon Jan  8 15:17:05 2018
#-- Contains event types : 
#--   12715000 - 28 files - 521601 events - 161.16 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-124834 

#--  StepId : 124834 
#--  StepName : Reco14a for MC 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v43r2p7 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/DataType-2012.py;$APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : sim-20141210-1-vc-mu100 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 


#--  Processing Pass Step-127160 

#--  StepId : 127160 
#--  StepName : Stripping21-NoPrescalingFlagged for Sim08 - MU - Implicit merging. 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v36r1p1 
#--  OptionFiles : $APPCONFIGOPTS/DaVinci/DV-Stripping21-Stripping-MC-NoPrescaling.py;$APPCONFIGOPTS/DaVinci/DV-RedoCaloPID-Stripping21.py;$APPCONFIGOPTS/DaVinci/DataType-2012.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : sim-20141210-1-vc-mu100 
#--  ExtraPackages : AppConfig.v3r205 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['/eos/lhcb/user/p/pluca/Analysis/B2KTauMu/Data/Bu2KTauMu_MC12.dst'], clear=True)
