isTest = False

import os, sys
lbroot = os.getenv("B2KTAUMUROOT")
if lbroot is not None : sys.path.append(lbroot+"/Options" )
sys.path.append(os.getcwd())

import B2KTauMuOption as opt
from DV_Config import ConfigDaVinci

from DV_Routines import ReStrip
lines_to_restrip = [ 
        'StrippingB2XTauMu_K_3pi_looseLine',
        'StrippingB2XTauMu_K_3pi_looseWSLine'
        ]

restrip, restripSq = ReStrip(lines_to_restrip,"stripping21r0p1",streamname="Leptonic")

opt.setalgs(True,'Bu2KTauMu3pi')
ConfigDaVinci("MC",12,opt.algs,Mag='MD',restrip=restripSq,isTest=isTest)



