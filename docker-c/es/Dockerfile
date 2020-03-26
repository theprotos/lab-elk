#FROM ubuntu:latest
FROM dockerc_es1
MAINTAINER vlad

ENV ES_SKIP_SET_KERNEL_PARAMETERS true

#RUN apt-get update -qq

# Elastic
RUN curl -L -o /tmp/elasticsearch-5.3.1.deb https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.3.1.deb
RUN dpkg -i /tmp/elasticsearch-5.3.1.deb
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install x-pack --batch
RUN sh -c "echo \"xpack.security.enabled: false\" >> /etc/elasticsearch/elasticsearch.yml"

# Cerebro
RUN curl -L -o /tmp/cerebro-0.6.5.tgz https://github.com/lmenezes/cerebro/releases/download/v0.6.5/cerebro-0.6.5.tgz
RUN tar -xzf /tmp/cerebro-0.6.5.tgz -C /tmp/
#RUN rm -f /tmp/cerebro-0.6.5.tgz
RUN mv /tmp/cerebro-0.6.5 /usr/share/elasticsearch/cerebro

EXPOSE 8000 9000 9200 9300
