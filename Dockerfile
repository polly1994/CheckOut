FROM ubuntu:16.04
MAINTAINER Pengpeng Zhou

RUN apt-get update
RUN apt-get install -y git python python-dev vim python-pip
RUN pip install pymongo

RUN ln -sf python2.7 python


# Install MongoDB.
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
  apt-get update && \
  apt-get install -y mongodb-org && \
  rm -rf /var/lib/apt/lists/*


# Create a non-root user for the checkout program
RUN /usr/sbin/useradd --create-home --home-dir /home/checkout --shell /bin/bash checkout

# Define mountable directories.
VOLUME ["/data/db"]

# Define default command.
CMD ["mongod"]

# Switch user
USER cashier

# Set home environment variable
ENV HOME /home/checkout

# Clone project from github
WORKDIR /home/checkout
RUN git clone https://github.com/polly1994/CheckOut.git

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 28017

#change working directory 
WORKDIR /home/checkout/CheckOut
