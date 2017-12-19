wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
chmod +x Miniconda-latest-Linux-x86_64.sh
./Miniconda-latest-Linux-x86_64.sh -b
source ~/.bashrc 
conda update conda
conda create -n snake -c bioconda python=3.4 snakemake beautiful-soup pyyaml

