# Use Ubuntu 16.04 LTS
FROM ubuntu:xenial-20181218

## Install dependencies including exfat libraries for exfat-formatted hard-drives (only MAC?) : exfat-fuse exfat-utils

RUN apt-get update && apt-get -qq -y install xvfb locate exfat-fuse exfat-utils apt-transport-https ca-certificates curl gnupg-agent software-properties-common

## Install miniconda3
RUN curl -sSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -bfp /opt/conda && \
    rm -rf /tmp/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda update conda && \
    conda clean --all --yes

## Install the conda environment
ADD environment.yml /app/environment.yml
RUN conda env create -f /app/environment.yml

ENV CONDA_ENV supermri-env 

ADD pymialsrtk/ /app/pymialsrtk/
ADD setup.py /app/setup.py
WORKDIR app/
RUN /bin/bash -c ". activate $CONDA_ENV && \
    python setup.py install"

## Install Docker engine
#RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
#RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#RUN apt-get update && apt-get -qq -y install docker-ce docker-ce-cli containerd.io

## Add Docker group
#RUN dockerd && docker pull sebastientourbier/mialsuperresolutiontoolkit