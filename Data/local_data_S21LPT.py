import os
from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(
        ['/eos/lhcb/user/p/pluca/Analysis/B2KTauMu/Data/CL12S21.leptonic.mdst']
        , clear=True)


