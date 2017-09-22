## Define root variable
export B2KTAUMUROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

## Setup the submodules
#source $B2KTAUMUROOT/tools-easyanalysis/setup.sh

## Setup with Snakemake or without
if [ "$1" = "snake" ]; then
    echo "Setup with snakemake"
    source activate snake
elif [[ $HOSTNAME != *"vm"* ]]; then #if I run on the virtual machine I want my own ROOT and python environment
    echo "Setup without snakemake"
    source $B2KTAUMUROOT/scripts/setup_path.sh
elif [[ $HOSTNAME == *"vm"* ]]; then
    echo "Setup without snakemake on Guido's VM"
    source $B2KTAUMUROOT/scripts/setup_path_guido.sh
fi

export PYTHONPATH=$B2KTAUMUROOT:$LCANAROOT:$B2KTAUMUROOT/Option:$B2KTAUMUROOT/Ganga:$B2KTAUMUROOT/python:$PYTHONPATH

# Locations

export PYTHONPATH=$B2KTAUMUROOT/python:$PYTHONPATH
export LUCAANAEOSLOC=/eos/lhcb/user/p/pluca/Analysis/
export RAPIDSIM_ROOT=$B2KTAUMUROOT/RapidSim

#export LBTUPLELOC=$EOSANALOC/Lb2emu/Tuple/
export LBLUCAJOBLOC=/eos/lhcb/user/p/pluca/ganga/

#export SCRIPTS=$B2KTAUMUROOT/scripts
export PLOTS=$B2KTAUMUROOT/plots
export TABLES=$B2KTAUMUROOT/tables

## Ganga

setupganga() {
    if [ -z "$GANGASYSROOT" ]; then
        source SetupProject.sh Ganga v602r3
    fi
}

## Aliases

alias goB2KTauMu='cd $B2KTAUMUROOT'
alias runganga='ganga -i $B2KTAUMUROOT/Ganga/gangaoption.py'

## Variables and aliases for snakemake

#alias setpath='source $LCANAROOT/scripts/setup_path.sh'
#export PY2='/afs/cern.ch/sw/lcg/releases/LCG_79/Python/2.7.9.p1/x86_64-slc6-gcc49-opt/bin/python'
alias snakeclean='rm $(snakemake --summary | tail -n+2 | cut -f1)'

#alias testDataTuple='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_Data.py $B2KTAUMUROOT/Data/local_data.py'
#alias testMCTuple='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_MC.py $B2KTAUMUROOT/Data/local_MC.py'


