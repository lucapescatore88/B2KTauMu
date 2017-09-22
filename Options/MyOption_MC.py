isTest = False

import os, sys
lbroot = os.getenv("B2KTAUMUROOT")
if lbroot is not None : sys.path.append(lbroot+"/Options" )
sys.path.append(os.getcwd())

import B2KTauMuOption as opt
from DV_Config import ConfigDaVinci

opt.setalgs(True,'Lb_JpsiL_ee')
ConfigDaVinci("MC",16,opt.algs,Mag='MD',restrip=[],isTest=isTest)


