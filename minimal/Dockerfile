# Docker stub modified from 
# https://github.com/esycat/docker-ubuntu/blob/master/Dockerfile
FROM ubuntu:18.04

ENV LANG C.UTF-8

# OS update, then clean up
RUN apt-get -yq update && \
    apt-get -yq upgrade && \
    apt-get -yq --no-install-recommends install \
        software-properties-common \
        apt-transport-https \
        ca-certificates \
        aptitude \
        wget \
        unzip && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/archive/* /var/lib/apt/lists/*

#FROM continuumio/miniconda3
#RUN conda create -n env python=3.6
#RUN echo "source activate env" > ~/.bashrc
#ENV PATH /opt/conda/envs/env/bin:$PATH
