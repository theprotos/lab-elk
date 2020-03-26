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
sudo sh -c "echo \"node.data: false\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"node.name: data4\" >> /etc/elasticsearch/elasticsearch.yml"
sudo sh -c "echo \"network.host: 192.168.100.14\" >> /etc/elasticsearch/elasticsearch.yml"
sudo systemctl start elasticsearch.service
sudo service elasticsearch restart


echo "|\/\/\/\/\/\| INSTALLING KIBANA |/\/\/\/\/\/|"
sudo wget -q -N ${kibanaURL}
sudo rpm --install ${kibanaPackage}
sudo sh -c "echo \"server.port: 9999\" >> /etc/kibana/kibana.yml"
sudo sh -c "echo \"server.host: 192.168.100.14\" >> /etc/kibana/kibana.yml"
sudo sh -c "echo \"elasticsearch.url: http://192.168.100.14:9200\" >> /etc/kibana/kibana.yml"
#sudo /usr/share/elasticsearch/kibana/bin/kibana-plugin install x-pack
sudo systemctl daemon-reload
sudo systemctl enable kibana
sudo systemctl start kibana
#rm -r ${kibanaPackage}


sudo sh -c "echo \"node.name: node1\" >> /etc/logstash/logstash.yml"
sudo sh -c "echo \"http.host: 192.168.100.14\" >> /etc/logstash/logstash.yml"
sudo sh -c "echo \"input {
  file {
    path           => '/var/log/messages'
    start_position => beginning
  }
}
output {
  elasticsearch {
    hosts => ['192.168.100.14:9200']
    index => 'logs-%{+YYYY.MM.dd}'
    sniffing => true
  }
  stdout { codec => rubydebug }
}

\" >> /etc/logstash/conf.d/01-syslog-input.conf"
sudo systemctl start logstash