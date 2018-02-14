print ("Testing")
import sys

f = open('log','w')

f.write(sys.version_info.__repr__())

print ("Looking for libraries")
import pyutils
import ROOT

f.write('\npyutils and ROOT imported ok\n')
f.write('Trying to read some files from eos\n')

print ("Looking for files")
import B2KTauMu as an
files = an.utils.remotels.remote_ls_fromids(an.dataids['CL11'])
f.write("Found %i files\n" % len(files))
f.write('\n'.join(files))
f.close()



