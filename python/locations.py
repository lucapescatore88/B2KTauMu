################## Location in repository or on EOS
import os
repo = os.getenv('B2KTAUMUROOT')

class loc : pass
loc.ROOT       = repo
loc.PYTHON     = loc.ROOT+'/python/'
loc.PLOTS      = loc.ROOT+'/plots/'
loc.LHCB       = loc.ROOT+'/LHCb/'
loc.TMPS       = loc.ROOT+'/tables/templates/'
loc.TABS       = loc.ROOT+'/tables/'
loc.TUPLE      = os.getenv('LBTUPLELOC')
loc.LUCAJOBS   = os.getenv('LBLUCAJOBLOC')
loc.LUCAANAEOS = os.getenv('LUCAANAEOSLOC')
loc.TMP        = repo

### Raw data locations

dataids = { 

        'CL11'           :(loc.LUCAJOBS, [602,603]),
        'CL12'           :(loc.LUCAJOBS, [604,605]),
        'CL15'           :(loc.LUCAJOBS, [610,607]),
        'CL16'           :(loc.LUCAJOBS, [608,609]),

        'CL11_BH'        :(loc.LUCAJOBS, [691,692]),
        'CL12_BH'        :(loc.LUCAJOBS, [693,694]),
        'CL15_BH'        :(loc.LUCAJOBS, [646,647]),
        'CL16_BH'        :(loc.LUCAJOBS, [648,649]),

        'MC12_Bu2KTauMu3pi'    : (loc.LUCAJOBS, [734,735]),
        'MC11_Bu2KTauMu3pi'    : (loc.LUCAJOBS, [749,750]),
        'MC12_Bu2KTauMu3pipi0' : (loc.LUCAJOBS, [751,752]),
        'MC11_Bu2KTauMu3pipi0' : (loc.LUCAJOBS, [753,754])

          }


