docker images
docker search ubuntu
docker pull ubuntu-upstart

docker build -f /path/to/a/Dockerfile .

docker rm $(docker ps -a -q)
docker rmi $(docker images -q)

docker build -t docker:java -f docker/Dockerfile-java .
docker build -t docker:openjdk -f docker/Dockerfile-openjdk .
docker build -t docker:logstash -f docker/Dockerfile-logstash .

docker run -i -t ubuntu:latest /bin/bash apt-get update


docker network ls
