import os
from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(
        ['/eos/lhcb/user/m/mmulder/Lb2Lee/DSTs/00051181_00036126_1.leptonic.mdst']
        , clear=True)


