#-- GAUDI jobOptions generated on Thu Jan 26 09:49:28 2017
#-- Contains event types : 
#--   90000000 - 14685 files - 4769337267 events - 57523.55 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-130112 

#--  StepId : 130112 
#--  StepName : Stripping26-Merging-DV-v41r2-AppConfig-v3r292-LZMA4-Compression 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v41r2 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py;$APPCONFIGOPTS/Persistency/Compression-LZMA-4.py 
#--  DDDB : dddb-20150724 
#--  CONDDB : cond-20161004 
#--  ExtraPackages : AppConfig.v3r292;SQLDDDB.v7r10 
#--  Visible : N 


#--  Processing Pass Step-129945 

#--  StepId : 129945 
#--  StepName : Stripping26-Merging-DV-v41r2-AppConfig-v3r289-LZMA4-Compression 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v41r2 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py;$APPCONFIGOPTS/Persistency/Compression-LZMA-4.py 
#--  DDDB : dddb-20150724 
#--  CONDDB : cond-20160522 
#--  ExtraPackages : AppConfig.v3r289;SQLDDDB.v7r10 
#--  Visible : N 


#--  Processing Pass Step-129716 

#--  StepId : 129716 
#--  StepName : Stripping26-Merging-DV-v40r2p1-AppConfig-v3r277-LZMA4-Compression 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v40r2p1 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py;$APPCONFIGOPTS/Persistency/Compression-LZMA-4.py 
#--  DDDB : dddb-20150724 
#--  CONDDB : cond-20160522 
#--  ExtraPackages : AppConfig.v3r277;SQLDDDB.v7r10 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles([
#'/afs/cern.ch/work/p/pluca/00059558_00000278_1.leptonic.mdst'
'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000278_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000291_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000296_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000298_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000322_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000324_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000334_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000345_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000365_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000368_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000371_1.leptonic.mdst',
#'LFN:/lhcb/LHCb/Collision16/LEPTONIC.MDST/00059558/0000/00059558_00000373_1.leptonic.mdst'


], clear=True)
