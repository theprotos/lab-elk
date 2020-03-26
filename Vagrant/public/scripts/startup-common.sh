#!/bin/bash
#=============================================================
#description:   .
#author:        vlad2211
#date:          4/11/16
#version:       .
#usage:         .
#notes:         .
#=============================================================
. ../config/profile.cfg

#Required
sudo systemctl restart network

#sudo yum update -y
echo "|\/\/\/\/\/\| INSTALLING PREREQUISITES |/\/\/\/\/\/|"
sudo yum install -y ${packagesInstall}
#sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch

echo "|\/\/\/\/\/\| INSTALLING ELASTICSEARCH |/\/\/\/\/\/|"
sudo wget -q -N ${ELKURL}
sudo rpm --install ${ELKPackage}
#rm -f ${ELKPackage}
sudo sh -c "echo \"cluster.name: mycluster\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"http.port: 9200\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"discovery.zen.ping.unicast.hosts: ["192.168.100.10", "192.168.100.11", "192.168.100.12", "192.168.100.13", "192.168.100.14"]\" >> /etc/elasticsearch/elasticsearch.yml"
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service


echo "|\/\/\/\/\/\| INSTALLING LOGSTASH |/\/\/\/\/\/|"
sudo chmod +r /var/log/messages
sudo wget -q -N ${logstashURL}
sudo rpm --install ${logstashPackage}
sudo systemctl daemon-reload
sudo systemctl enable logstash.service


#sudo java -version
