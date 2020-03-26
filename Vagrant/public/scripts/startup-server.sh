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

sudo sh -c "echo \"node.master: true\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"node.data: false\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"node.name: master\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"network.host: 192.168.100.10\" >> /etc/elasticsearch/elasticsearch.yml"
#sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu
#sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install x-pack
sudo systemctl start elasticsearch.service
sudo service elasticsearch start

sudo sh -c "echo \"node.name: server\" >> /etc/logstash/logstash.yml"
sudo sh -c "echo \"http.host: 192.168.100.10\" >> /etc/logstash/logstash.yml"
sudo sh -c "echo \"input {
  file {
    path           => '/var/log/messages'
    start_position => beginning
  }
}
output {
  elasticsearch {
    hosts => ['192.168.100.10:9200']
    index => 'logs-%{+YYYY.MM.dd}'
    sniffing => true
  }
  stdout { codec => rubydebug }
}\" > /etc/logstash/conf.d/01-syslog-input.conf"
sudo systemctl start logstash
