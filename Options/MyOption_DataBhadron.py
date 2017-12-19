isTest = True
test = ""
if isTest : test = "Test"

import os, sys
root = os.getenv("B2KTAUMUROOT")
if root is not None : 
    sys.path.append(root+"/Options" )
sys.path.append(os.getcwd())

import B2KTauMuOption as opt
from DV_Config import ConfigDaVinci

opt.setalgs()
ConfigDaVinci("CL",16,opt.algs,Mag=test,RootInTES="Bhadron",isTest=isTest)


