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
        apt-utils \
        aptitude \
        wget \
        unzip && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/archive/* /var/lib/apt/lists/*

FROM continuumio/miniconda3
ADD ./environment.yml /
RUN conda update -n base conda -y && conda env update

