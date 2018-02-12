configfile : 'cfg.yml'
print('CONFIGURATION:',config)

shell.executable("/bin/bash")
if config['cvmfs'] == 'True' :
    shell.prefix('cd $B2KTAUMUROOT && source setup.sh && ')
else :
    shell.prefix('cd $B2KTAUMUROOT && source setup.sh venv && ')

rule test :
    input  : ['python/test.py']
    output : ['log']
    shell : "python {input} && cat log "

include : "snake/testDV.snake"
include : "snake/cut.snake"

