## Snakemake

Snakemake is a pipeline tool that allows to run several step of the analysis in an organised way.
This may require a little effort to setup but saves a LOT of work overtime.

Snakemake tutorial: https://snakemake.bitbucket.io/snakemake-tutorial.html (start from Basics Step 1)

### First installation

Snakemake is not installed on lxplus so the first time you use it you have to install it by yourself.
On lxplus or machines with CVMFS installed the following should be enough.

N.B.: This needs to be done **before** sourcing setup.sh.

```
wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
chmod +x Miniconda-latest-Linux-x86_64.sh
./Miniconda-latest-Linux-x86_64.sh
source ~/.bashrc (or re-login)
conda update conda
conda create -n snake -c bioconda python=3.4 snakemake beautiful-soup pyyaml
```


