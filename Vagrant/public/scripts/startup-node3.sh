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

sudo sh -c "echo \"node.master: false\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"node.data: true\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"node.name: data3\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"network.host: 192.168.100.13\" >> /etc/elasticsearch/elasticsearch.yml"

sudo systemctl start elasticsearch.service
sudo service elasticsearch restart

sudo sh -c "echo \"node.name: node3\" >> /etc/logstash/logstash.yml"
sudo sh -c "echo \"http.host: 192.168.100.13\" >> /etc/logstash/logstash.yml"
sudo sh -c "echo \"input {
  file {
    path           => '/var/log/messages'
    start_position => beginning
  }
}
output {
  elasticsearch {
    hosts => ['192.168.100.13:9200']
    index => 'logs-%{+YYYY.MM.dd}'
    sniffing => true
  }
  stdout { codec => rubydebug }
}

\" >> /etc/logstash/conf.d/01-syslog-input.conf"
sudo systemctl start logstash
