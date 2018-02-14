## Define root variable
export B2KTAUMUROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"

if [ -e $B2KTAUMUROOT/tools-easyanalysis/lib/libtools.so ]
   then
       echo "Tools already compiled"
   else
       echo "Compiling tools"
       echo $1
       source scripts/setup.sh $1
       cd $B2KTAUMUROOT/tools-easyanalysis
       unset TOOLSSYS
       source scripts/setup.sh
       make shared
       cd $B2KTAUMUROOT
fi


set +u

## Setup with Snakemake or without
if [ "$1" == "snake" ]; then
    echo "Setup with snakemake"
    source activate snake
elif [ "$1" == "venv" ]; then 
    echo "Setup with venv"
    source $B2KTAUMUROOT/scripts/setup_venv.sh
    cd $B2KTAUMUROOT/tools-easyanalysis
    unset TOOLSSYS
    source scripts/setup.sh
    cd $B2KTAUMUROOT
elif [ "$1" == "none" ]; then
    echo "Setup without snakemake, venv and cvmfs"
elif [ "$1" == "novenv" ]; then
    echo "Setup without venv"
    source $B2KTAUMUROOT/scripts/setup_path.sh
    cd $B2KTAUMUROOT/tools-easyanalysis
    unset TOOLSSYS
    source scripts/setup.sh
    cd $B2KTAUMUROOT
else
    echo "Setup with cvmfs"
    source $B2KTAUMUROOT/scripts/setup_path.sh
    source $B2KTAUMUROOT/scripts/setup_venv.sh
    cd $B2KTAUMUROOT/tools-easyanalysis
    unset TOOLSSYS
    source scripts/setup.sh
    cd $B2KTAUMUROOT

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
alias snakeclean='rm $(snakemake --summary | tail -n+2 | cut -f1)'

alias testData_CL16LPT='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_DataLeptonic.py $B2KTAUMUROOT/Data/local_data_S28LPT.py'
alias testData_CL12LPT='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_DataLeptonic.py $B2KTAUMUROOT/Data/local_data_S21LPT.py'
alias testData_CL16BH='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_DataBhadron.py $B2KTAUMUROOT/Data/local_data_S28BH.py'
alias testData_CL12BH='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_DataBhadron.py $B2KTAUMUROOT/Data/local_data_S21BH.py'
alias testMCTuple='lb-run DaVinci/latest gaudirun.py $B2KTAUMUROOT/Options/MyOption_MC.py $B2KTAUMUROOT/Data/testMC.py'


