FROM ubuntu:14.04

#Install some
RUN apt-get clean
RUN apt-get update
RUN apt-get install -y g++
RUN apt-get install -y openssh-server vim git python3 python3-dev python3-pip
RUN pip3 install pymongo 
RUN mkdir -p /var/run/sshd

#open port 22
EXPOSE 22
#CMD ["/usr/sbin/sshd", "-D"]


RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
ENV MONGO_MAJOR 3.0
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list
# Install MongoDB
RUN apt-get update
RUN sudo apt-get install -y mongodb-org=3.0.4 mongodb-org-server=3.0.4 mongodb-org-shell=3.0.4 mongodb-org-mongos=3.0.4 mongodb-org-tools=3.0.4

# Create the MongoDB data directory
RUN mkdir -p /data/db

RUN git clone https://github.com/polly1994/CheckOut.git

#open port 27017 
EXPOSE 27017
ENTRYPOINT ["usr/bin/mongod"]
