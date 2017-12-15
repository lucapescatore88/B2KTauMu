FROM rootproject/root-ubuntu16

MAINTAINER Luca Pescatore <luca.pescatore@cern.ch>

# install basic libraries
USER root

## Kerberos configuration
ADD krb5.conf /etc/krb5.conf
ADD mykey.keytab /root/mykey.keytab
ADD scripts/run_kinit.sh /root/run_kinit.sh

## Install extra packages
RUN apt-get -y update \
    && apt-get -y install wget

RUN apt-get -y update \
    && apt-get -y install build-essential libx11-dev libxpm-dev libxft-dev libxext-dev libpng12-dev libjpeg-dev gfortran libssl-dev libpcre3-dev libgl1-mesa-dev libglew1.5-dev libftgl-dev libmysqlclient-dev libfftw3-dev libcfitsio3-dev graphviz-dev libavahi-compat-libdnssd-dev libldap2-dev libxml2-dev libafterimage0 libafterimage-dev cmake vim emacs git zsh 

RUN apt-get -y update && apt-get -y install krb5-user openssh-server krb5-config

RUN apt-get -y update \
    && apt-get -y install libboost-all-dev

# gsl and clang
RUN apt-get -y update && apt-get -y upgrade \
    && apt-get -y install libgsl2 clang
#    && apt-get -y install libgsl0ldbl libgsl0-dev clang

# XRootD
RUN git clone --depth 1 http://github.com/xrootd/xrootd.git -b v4.7.1 --single-branch \
    && mkdir xrootd-build \
    && cd xrootd-build \
    && cmake ../xrootd -DCMAKE_INSTALL_PREFIX=/usr/local -DENABLE_PERL=FALSE -DENABLE_FUSE=FALSE -DENABLE_KRB5=TRUE \
    && make && make install \
    && cd .. && rm -rf xrootd xrootd-build

RUN apt-get -y update \
    && apt-get -y install graphviz exiv2 exiftool

ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
ENV PYTHONPATH /usr/local/lib:$PYTHONPATH


# install conda to manage auxilliary packages
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda-3.16.0-Linux-x86_64.sh && \
    /bin/bash Miniconda-3.16.0-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda-3.16.0-Linux-x86_64.sh && \
    /opt/conda/bin/conda install --yes conda==3.18.3

ENV PATH /opt/conda/bin:$PATH

# this will be our main environment
RUN conda update conda
RUN conda create -y -f -n snake -c bioconda python=3.4 beautiful-soup=4.3.2 pyyaml=3.12
# RUN conda install -n snake -c anaconda jinja2=2.9.6
RUN conda install -n snake -c https://conda.anaconda.org/conda-forge gitpython
RUN conda install -n snake -c https://conda.anaconda.org/anaconda pytz=2016.10
RUN conda install -n snake -c bioconda snakemake=3.10.0
RUN conda install scikit-learn
RUN pip install virtualenv virtualenvwrapper
#RUN conda install -n snake scikit-learn


# in order to be able to push to a repository you need to set your git identity
RUN git config --global user.email "luca.pescatore@cern.ch" && \
    git config --global user.name "Luca Pescatore" && \
    git config --global push.default simple


# Add authentication files (add more if needed)
RUN mkdir /root/.ssh
ADD id_rsa /root/.ssh/id_rsa
#ADD id_cirunner /root/.ssh/id_cirunner
RUN chmod 700 /root/.ssh
RUN chmod 700 /root/.ssh/id_rsa
#RUN chmod 700 /root/.ssh/id_cirunner
# add them to the ssh configuration
RUN echo "Host gitlab gitlab.cern.ch\n    Hostname gitlab.cern.ch\n     StrictHostKeyChecking=no\n\n" | cat - /etc/ssh/ssh_config > tmp.txt && \
    mv tmp.txt /etc/ssh/ssh_config && \
    echo "    IdentityFile ~/.ssh/id_rsa\n    StrictHostKeyChecking=no" >> /etc/ssh/ssh_config
#     IdentityFile ~/.ssh/id_cirunner\n    StrictHostKeyChecking=no\n\n" | cat - /etc/ssh/ssh_config > tmp.txt && \


### Specific to B2Ktaumurepo

RUN git clone --recursive ssh://git@gitlab.cern.ch:7999/LHCb-RD/vrd-B2KTauMu.git

ENV B2KTAUMUROOT /vrd-B2KTauMu
ADD scripts/anasetup.sh $B2KTAUMUROOT/anasetup.sh
RUN cd $B2KTAUMUROOT && chmod +x $B2KTAUMUROOT/anasetup.sh && /bin/bash $B2KTAUMUROOT/anasetup.sh

ENV VENVSYS $B2KTAUMUROOT/python/venv
ADD scripts/set_venv.sh $B2KTAUMUROOT/set_venv.sh
RUN cd $B2KTAUMUROOT && /opt/conda/bin/virtualenv -p `which python2.7` $VENVSYS \
    && chmod +x B2KTAUMUROOT/set_venv.sh && B2KTAUMUROOT/set_venv.sh

CMD ["bash"]


