FROM ubuntu:latest
MAINTAINER vlad

ENV DEBIAN_FRONTEND noninteractive
ENV ES_SKIP_SET_KERNEL_PARAMETERS true

RUN mkdir /apps
WORKDIR /apps

RUN apt-get update -qq
# Optional packages
RUN apt-get install -y -qq dialog apt-utils net-tools iputils-ping
RUN apt-get install -y -qq software-properties-common python-software-properties curl git debconf-utils
RUN apt-get install -y -qq openjdk-8-jre openjdk-8-jdk

# Python
RUN apt-get install -y -qq python-pip
RUN pip install flask
RUN pip install redis
RUN pip install --upgrade pip