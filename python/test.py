import sys

f = open('log','w')

f.write(sys.version_info.__repr__())

import pyutils
import ROOT

f.write('\npyutils and ROOT imported ok\n')
f.write('Trying to read some files from eos\n')

import B2KTauMu as an
files = an.utils.remote_ls_fromids(an.dataids['CL11'])

f.write('\n'.join(files))
f.close()



