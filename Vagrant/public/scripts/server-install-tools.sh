#!/bin/bash

. ../config/profile.cfg

# Install
# Bash+XML
sudo yum install -y epel-release
#sudo yum install -y xmlstarlet
echo "Install Jenkins dependencies"
sudo yum install -y git ant ant-junit maven java-1.6.0-openjdk-devel java-1.7.0-openjdk java
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum install -y jenkins

echo "Config Startup"
sudo chkconfig jenkins on
sudo service jenkins start

exit 0
