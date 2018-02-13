import os, re
from pyutils.processing.submit import launch_job, parser
from glob import glob
from B2KTauMu.utils import remotels as rem
from B2KTauMu import loc
from locations import dataids

parser.add_argument('dtype',default='CL12')
parser.add_argument('--test',action="store_true")
parser.add_argument('--nevt',type=int,default=-1)
parser.add_argument('--odir',default=loc.TMP)
parser.add_argument('--group',type=int,default=30)
parser.add_argument('--tree',default='B2KTauMu_pmpTuple/DecayTree')
opts = parser.parse_args()

print "Looking for files on eos: ", dataids[opts.dtype]
tmpfiles = rem.remote_ls_fromids(dataids[opts.dtype])

## Split files in groups
if opts.group > 1 :
    files = [' '.join(tmpfiles[i:i + opts.group]) for i in range(0, len(tmpfiles), opts.group)]

for fi,f in enumerate(files) :

    cmd = "python $B2KTAUMUROOT/python/B2KTauMu/utils/cut_tree.py -t {tree} -f {files} -n {nick} -e {nevt} -d {dtype} -o {odir} "
    opts.command = cmd.format(tree=opts.tree.replace(" ",""),files=f,nevt=opts.nevt,dtype=opts.dtype,odir=opts.odir,nick=str(fi))
    if opts.test : opts.command += " --test "
    opts.abspath = True
    opts.setup = "export CDIR=$PWD && source $B2KTAUMUROOT/setup.sh && cd $CDIR "
    
    ids = re.findall(r'/(\d+)/(\d+)/',f)
    opts.basedir = opts.odir
    if not os.path.exists(opts.basedir) : os.makedirs(opts.basedir)
    opts.subdir  = opts.dtype
    opts.jobname = str(fi)
    
    launch_job(opts)


