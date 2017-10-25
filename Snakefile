rule test :
    input  : ['python/test.py']
    output : ['log']
    shell : "cd $B2KTAUMUROOT && source setup.sh XX && $PY2 {input}"
