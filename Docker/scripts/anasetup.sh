source /root/run_kinit.sh

if [ "$1" = "snake" ]; 
    then
        echo "Setup with snakemake"
        source activate snake
        export PYTHONPATH=$B2KTAUMUROOT/python:$B2KTAUMUROOT/pyutils:$B2KTAUMUROOT
    else
        source $B2KTAUMUROOT/setup_env.sh
fi
