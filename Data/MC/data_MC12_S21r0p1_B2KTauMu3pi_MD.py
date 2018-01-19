#-- GAUDI jobOptions generated on Fri Jan 19 14:20:23 2018
#-- Contains event types : 
#--   12112000 - 203 files - 506363 events - 123.74 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-128579 

#--  StepId : 128579 
#--  StepName : TCK-0x409f0045 Flagged for Simulation 2012 (L0 separate step) 
#--  ApplicationName : Moore 
#--  ApplicationVersion : v14r8p1 
#--  OptionFiles : $APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep.py;$APPCONFIGOPTS/Conditions/TCK-0x409f0045.py;$APPCONFIGOPTS/Moore/DataType-2012.py 
#--  DDDB : dddb-20170721-2 
#--  CONDDB : sim-20160321-2-vc-md100 
#--  ExtraPackages : AppConfig.v3r241 
#--  Visible : Y 


#--  Processing Pass Step-130329 

#--  StepId : 130329 
#--  StepName : Reco14c for MC - 2012 - to be used with Sim09 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v43r2p11 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/DataType-2012.py;$APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Brunel/Sim09-Run1.py;$APPCONFIGOPTS/Persistency/DST-multipleTCK-2012.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20170721-2 
#--  CONDDB : sim-20160321-2-vc-md100 
#--  ExtraPackages : AppConfig.v3r307 
#--  Visible : Y 


#--  Processing Pass Step-125934 

#--  StepId : 125934 
#--  StepName : L0 emulation - TCK 0045 
#--  ApplicationName : Moore 
#--  ApplicationVersion : v20r4 
#--  OptionFiles : $APPCONFIGOPTS/L0App/L0AppSimProduction.py;$APPCONFIGOPTS/L0App/L0AppTCK-0x0045.py;$APPCONFIGOPTS/L0App/DataType-2012.py 
#--  DDDB : dddb-20170721-2 
#--  CONDDB : sim-20160321-2-vc-md100 
#--  ExtraPackages : AppConfig.v3r200 
#--  Visible : N 


#--  Processing Pass Step-129453 

#--  StepId : 129453 
#--  StepName : Stripping21r0p1-NoPrescalingFlagged for Sim09 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v39r1p1 
#--  OptionFiles : $APPCONFIGOPTS/DaVinci/DV-Stripping21r0p1-Stripping-MC-NoPrescaling.py;$APPCONFIGOPTS/DaVinci/DV-RedoCaloPID-Stripping21.py;$APPCONFIGOPTS/DaVinci/DataType-2012.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py 
#--  DDDB : dddb-20170721-2 
#--  CONDDB : sim-20160321-2-vc-md100 
#--  ExtraPackages : AppConfig.v3r277 
#--  Visible : Y 


#--  Processing Pass Step-132745 

#--  StepId : 132745 
#--  StepName : Digi14a for 2012 (to use w Sim09) 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v30r2p1 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/DataType-2012.py;$APPCONFIGOPTS/Boole/NoPacking.py;$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py 
#--  DDDB : dddb-20170721-2 
#--  CONDDB : sim-20160321-2-vc-md100 
#--  ExtraPackages : AppConfig.v3r342 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000001_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000002_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000003_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000004_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000005_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000006_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000007_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000008_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000009_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000010_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000011_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000012_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000014_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000015_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000016_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000017_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000018_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000019_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000020_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000021_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000022_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000023_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000024_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000025_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000026_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000027_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000028_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000029_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000030_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000031_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000032_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000033_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000034_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000035_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000036_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000037_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000038_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000039_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000040_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000041_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000042_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000043_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000044_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000045_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000046_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000047_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000048_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000049_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000050_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000051_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000052_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000053_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000054_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000055_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000056_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000058_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000059_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000060_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000061_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000062_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000063_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000064_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000065_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000066_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000067_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000068_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000069_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000070_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000071_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000072_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000073_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000074_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000075_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000076_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000077_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000078_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000079_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000080_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000081_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000082_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000083_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000084_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000085_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000086_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000087_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000088_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000089_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000090_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000091_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000092_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000093_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000094_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000095_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000096_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000097_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000098_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000099_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000100_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000101_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000102_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000103_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000104_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000105_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000106_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000107_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000108_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000109_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000110_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000111_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000112_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000113_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000114_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000115_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000116_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000117_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000118_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000119_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000120_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000121_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000122_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000123_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000124_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000125_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000126_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000127_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000128_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000129_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000130_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000131_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000132_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000133_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000134_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000135_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000136_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000137_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000138_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000139_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000140_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000141_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000142_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000143_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000144_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000145_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000146_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000147_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000148_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000149_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000150_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000151_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000152_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000153_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000154_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000155_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000156_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000157_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000158_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000159_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000160_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000161_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000162_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000163_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000164_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000165_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000166_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000167_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000168_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000169_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000170_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000171_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000172_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000174_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000175_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000176_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000177_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000178_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000179_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000180_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000181_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000182_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000183_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000184_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000185_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000186_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000187_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000188_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000189_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000190_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000191_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000192_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000193_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000194_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000195_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000196_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000197_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000198_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000199_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000200_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000201_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000202_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000203_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000204_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000205_5.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00069363/0000/00069363_00000206_5.AllStreams.dst'
], clear=True)
