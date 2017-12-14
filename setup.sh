## Define root variable
export B2KTAUMUROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

set +u

## Setup with Snakemake or without
if [ "$1" == "snake" ]; then
    echo "Setup with snakemake"
    source activate snake
elif [ "$1" == "env" ]; then 
    echo "Setup without snakemake"
    source $B2KTAUMUROOT/scripts/setup_path.sh
    source $B2KTAUMUROOT/scripts/setup_venv.sh
fi

cd $B2KTAUMUROOT/pyutils
source setup.sh
cd $B2KTAUMUROOT

export PYTHONPATH=$B2KTAUMUROOT:$B2KTAUMUROOT/Option:$B2KTAUMUROOT/Ganga:$B2KTAUMUROOT/python:$PYTHONPATH

# Locations

export LUCAANAEOSLOC=/eos/lhcb/user/p/pluca/Analysis/
export RAPIDSIM_ROOT=$B2KTAUMUROOT/RapidSim

export LBLUCAJOBLOC=/eos/lhcb/user/p/pluca/ganga/

export SCRIPTS=$B2KTAUMUROOT/scripts
export PLOTS=$B2KTAUMUROOT/plots
export TABLES=$B2KTAUMUROOT/tables

## Aliases

alias goB2KTauMu='cd $B2KTAUMUROOT'
alias runganga='ganga -i $B2KTAUMUROOT/Ganga/gangaoption.py'

## Variables and aliases for snakemake

#alias setpath='source $LCANAROOT/scripts/setup_path.sh'
export PY2=$B2KTAUMUROOT/python/venv/bin/python
alias snakeclean='rm $(snakemake --summary | tail -n+2 | cut -f1)'

#alias testDataTuple='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_Data.py $B2KTAUMUROOT/Data/local_data.py'
#alias testMCTuple='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_MC.py $B2KTAUMUROOT/Data/local_MC.py'


