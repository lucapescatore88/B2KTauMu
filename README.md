## What is this repository
------

This is a repository containing code for the analyis of the LFV B2KTauMu decay.

Contact: luca.pescatore@cern.ch, giulio.dujany@cern.ch

## How to setup the repository
------

Clone the repository.

```git clone ssh://git@gitlab.cern.ch:7999/pluca/B2Ktaumu.git```

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
------

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

All cuts should go into .py files in the folder `python/cuts/`. Mainly into `__init__.py`
These can be then used as e.g. :

```from B2KTauMu import *
data.Draw('Somevar',cuts.somecut)```

See also paragraph after.

### B2KTauMu python environment (important!!)

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

* Provide easy handling of output files, e.g.:

Create a file (only the first time)
```
import B2KTauMuEnv as an
an.outfiles.create("yields")                ## Will create the $B2KTAUMUROOT/tables/yields.txt
outfile.writeline("yields","N_B0 = 4000")   ## Now you can write stuff into it or... (see following)
```

Or even better use templates!!!

   - Crate a .tmp file in the tables/templates folder. You can write whatever you want into it just put the values to substitute into {}
   
   E.g.
   ```
   yield_signal = ${yield_sig} \pm {yield_sig_err}$
   ```
   
   And then fill it! (Will take by defulta the values saved in an.db)

```
import B2KTauMuEnv as an
an.outfile.fill_template("efficiencies","eff_tmp")
```
  
  This will look for the keys into the db, fill them into your template and same everything to $REPO/tables/efficiency.txt



### Snakemake

You can run the offline anaylsis (or parts of it) simply typing `snakemake`.
The steps are defined into `Snakefile` in the top folder. See README_SNAKEMAKE for more details.

To run snakemake from a clean shell:

```
source setup.ch snake
snakemake
```


## Common utilities
------

The `python/utils` folder contains utilities which you may find useful. See python/utils/README.md.


