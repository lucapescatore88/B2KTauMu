## What is this repository

This is a repository containing code for the analyis of the LFV B2KTauMu decay.

Contact: luca.pescatore@cern.ch, giulio.dujany@cern.ch

## How to setup the repository

Clone the repository.

```git clone --recursive ssh://git@gitlab.cern.ch:7999/pluca/B2Ktaumu.git```

If you want to run interactively in testing mode (normal way to run).

```source setup.sh```

Or if you want to run pipelines using Snakemake:

```source setup.sh snake ```

N.B.: To work properly in "snake" mode you have to setup some dependencies (Snakemake) the first time you use it.
Please read README_SNAKEMAKE.

### Environment

* The `B2KTAUMUROOT` variable is now avilable pointing to the top folder of the repo.
* ROOT, matplotlib, sklearn, etc are setup.
* Now code into the `python` folder should be automatically picked up if you try to import it.
* At the beginning of each python file you should add `import B2KTauMu as an` (see later)


## Repository Structure

* The analysis code should be contained into the `scripts` and `python` folders.

N.B.: If you make subfolders of `python` put an empty `__init__.py` file inside each one.
* `Ganga` contains Ganga options. In parituclar gangaoption.py where a function CreateDVJob()
is defied. 

Running ganga with `runganga` all functions defined in gangaoption.py will be available.
* `Options` contains DaVinci options to create the tuples.
* `Data` contains files with lists of LFNs used to make tuples.
* `LHCb` contains generic LHCb stuff like the LHCb style file and the particle propeties.
* `tables` is where you should put the output tables (see B2KTauMuEnv).

It also contains the `templates` folder which should contain latex templates to be filled automatically.
* `plots` is where you should put output splots (see B2KTauMuEnv).

### Cuts

All cuts should go into .py files in the folder `python/B2KTauMu/cuts/`. Mainly into `__init__.py`
These can be then used as e.g. :

```import B2KTauMu.cuts as cuts
data.Draw('Somevar',cuts.somecut)```

See also python environment paragraph.

### Access data

Raw data (the output of the stripping) can be accessed using a provided function:

```import B2KTauMu as an
files = an.utils.remote_ls_fromids(an.dataids['{some data label e.g. CL11}'])```

To see the available datasets: 

```import B2KTauMu as an
print an.dataids.keys()
['CL16', 'CL15', 'CL12', 'CL11']```

## B2KTauMu python environment (important!!)

This module loads the python environment: `import B2KTauMuEnv as an`.

What will this do for you:

* Checking that you sourced the setup.sh file.

* Loading the LHCb style for plots.

* Make available any variable defined into B2KTauMu/__init__.py (e.g. se next point: loc)

* Make the locations easily available to your pathon scripts though the `loc` object. Sone already defined locations are the following (feel free to define more as you need them):

    - loc.ROOT   = $LB2LEMUANAROOT
    - loc.PYTHON = $LB2LEMUANAROOT/python/
    - loc.LHCB   = $LB2LEMUANAROOT/LHCb/
    - loc.PLOTS  = $LB2LEMUANAROOT/plots/
    - loc.TABS   = $LB2LEMUANAROOT/tables/
    - loc.TMPS   = $LB2LEMUANAROOT/tables/templates/
    - loc.TUPLE  = /eos/lhcb/user/p/pluca/Analysis/B2KTauMu/Tuple/

* Provide a common database saved on disk to presist results, e.g.:.

```
import B2KTauMuEnv as an
print an.db
{'Test':True, ...}
an.db['myeff'] = 0.99
dumpDB() ## Saves it to disk
```

* Provide easy handling of output files

```from Lb2LemuEnv import *
outfiles.create("yields") ## Will create (only first time) the $LB2LEMUROOT/tables/yields.txt file and remember that it exists 
outfile.writeline("yields","N_B0 = 4000")```

Or even better you can do the same using templates!!! Crate a file in the templates folder. You can write whatever you want into it just put the values to substitute into {}
   
E.g.: `seleff = ${sel_eff} \pm {sel_eff_err}$`
   
And then use the `db` object to fill it!!

```from Lb2LemuEnv import *
outfile.fill_template("efficiencies","eff_tmp",db)```
 
This will look for the keys into the db, fill them into your template and same everything to $REPO/tables/efficiency.txt

* Make available to every script any other variable you wish to define into it. 


## Snakemake

You can run the offline anaylsis (or parts of it) simply typing `snakemake`.
The steps are defined into `Snakefile` in the top folder. See README_SNAKEMAKE for more details.

To run snakemake from a clean shell:

```
source setup.ch snake
snakemake
```
## Docker

Docker support is available for this repository to allow running the analysis on any machine anywhere in the world (with internet). Please have a look at the readme inside the Docker folder.

## Common utilities

The `pyutils` folder contains utilities which you may find useful. See pyutils/README.md.


