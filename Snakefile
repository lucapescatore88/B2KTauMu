sample = [1,5]

shell.prefix('cd $B2KTAUMUROOT && source setup.sh && ')

rule test :
    input  : ['python/test.py']
    output : ['log']
    shell : "python {input}"



