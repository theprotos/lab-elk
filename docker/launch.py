import datetime
import subprocess
import config
import time
import str

#//TODO: Docker compose


def dockerclean():
    containers = subprocess.getoutput(['docker', 'ps', '-a', '-q'])
    if containers:
        print("[DOCKER] Stop and remove all contaners: ")
        for container in containers.split():
            subprocess.call(["docker", "stop", container])
            subprocess.call(["docker", "rm", "-f", container])
    else:
        print("[DOCKER] No containers")


def buildimages(imagename, configfile):
    print("[DOCKER] Building image: " + imagename)
    subprocess.run(['docker', 'build', '-t', imagename, '-f', configfile, '.'])


def startcontainers(port1, port2, port3, port4, containername, imagename):
    print("[DOCKER] Starting container: " + containername)
    subprocess.run(['docker', 'run', '-d', '-i', '-p', port1, '-p', port2, '-p', port3, '-p', port4, '--name', containername, imagename])


def runcmdbash(containername, containercmd):
    print("[ELASTICSEARCH] Running " + containercmd + " on " + containername)
    subprocess.run(['docker', 'exec', "-t", "-d", containername, '/bin/bash', '-c', containercmd])


def runcmd(containername, containercmd, containercmdparam):
    print("[ELASTICSEARCH] Running " + containercmd + " on " + containername)
    #only to start ES and kibana
    subprocess.run(['docker', 'exec', containername, containercmd, containercmdparam])


start_time = time.clock()
print(str(datetime.datetime.now()) + " Started")

dockerclean()

buildimages(config.DOCKERIMAGE_OPENJDK, config.DOCKERFILE_OPENJDK)
buildimages(config.DOCKERIMAGE_ES, config.DOCKERFILE_ES)
buildimages(config.DOCKERIMAGE_KIBANA, config.DOCKERFILE_KIBANA)

startcontainers('9200:9200', '9300:9300', '8000:8000', '9000:9000', config.ES_NODES[0], config.DOCKERIMAGE_ES)
startcontainers('9210:9200', '9310:9300', '8010:8000', '9010:9000', config.ES_NODES[1], config.DOCKERIMAGE_ES)
startcontainers('9220:9200', '9320:9300', '8020:8000', '9020:9000', config.ES_NODES[2], config.DOCKERIMAGE_ES)
startcontainers('9230:9200', '9330:9300', '8030:8000', '9030:9000', config.ES_NODES[3], config.DOCKERIMAGE_ES)
startcontainers('9240:9200', '9340:9300', '8040:8000', '9040:9000', config.KIBANA_NODES[0], config.DOCKERIMAGE_KIBANA)
startcontainers('9250:9200', '9350:9300', '8050:8000', '9050:9000', config.KIBANA_NODES[1], config.DOCKERIMAGE_KIBANA)


for node in config.ES_NODES:
    runcmdbash(node, config.HTTP_PYTHON)


for node in config.KIBANA_NODES:
    runcmdbash(node, config.HTTP_PYTHON)


print("[ELASTICSEARCH] Configure elasticsearch.yml for elk0")
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[0], '/bin/bash', '-c', 'echo \"node.name: manager1\" > /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[0], '/bin/bash', '-c', 'echo \"cluster.name: mycluster\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[0], '/bin/bash', '-c', 'echo \"http.port: 9200\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[0], '/bin/bash', '-c', 'echo \"node.master: true\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[0], '/bin/bash', '-c', 'echo \"node.data: true\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[0], '/bin/bash', '-c', 'echo \"network.host: 172.17.0.2\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[0], '/bin/bash', '-c', 'echo \"discovery.zen.ping.unicast.hosts: ["172.17.0.2", "172.17.0.3", "172.17.0.4", "172.17.0.5", "172.17.0.6"]\" >> /etc/elasticsearch/elasticsearch.yml'])
print("[ELASTICSEARCH] Configure elasticsearch.yml for elk1")
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[1], '/bin/bash', '-c', 'echo \"node.name: manager2\" > /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[1], '/bin/bash', '-c', 'echo \"cluster.name: mycluster\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[1], '/bin/bash', '-c', 'echo \"http.port: 9200\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[1], '/bin/bash', '-c', 'echo \"node.master: true\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[1], '/bin/bash', '-c', 'echo \"node.data: true\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[1], '/bin/bash', '-c', 'echo \"network.host: 172.17.0.3\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[1], '/bin/bash', '-c', 'echo \"discovery.zen.ping.unicast.hosts: ["172.17.0.2", "172.17.0.3", "172.17.0.4", "172.17.0.5", "172.17.0.6"]\" >> /etc/elasticsearch/elasticsearch.yml'])
print("[ELASTICSEARCH] Configure elasticsearch.yml for elk2")
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[2], '/bin/bash', '-c', 'echo \"node.name: data2\" > /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[2], '/bin/bash', '-c', 'echo \"cluster.name: mycluster\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[2], '/bin/bash', '-c', 'echo \"http.port: 9200\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[2], '/bin/bash', '-c', 'echo \"node.master: false\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[2], '/bin/bash', '-c', 'echo \"node.data: true\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[2], '/bin/bash', '-c', 'echo \"network.host: 172.17.0.4\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[2], '/bin/bash', '-c', 'echo \"discovery.zen.ping.unicast.hosts: ["172.17.0.2", "172.17.0.3", "172.17.0.4", "172.17.0.5", "172.17.0.6"]\" >> /etc/elasticsearch/elasticsearch.yml'])
print("[ELASTICSEARCH] Configure elasticsearch.yml for elk3")
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[3], '/bin/bash', '-c', 'echo \"node.name: data2\" > /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[3], '/bin/bash', '-c', 'echo \"cluster.name: mycluster\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[3], '/bin/bash', '-c', 'echo \"http.port: 9200\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[3], '/bin/bash', '-c', 'echo \"node.master: false\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[3], '/bin/bash', '-c', 'echo \"node.data: true\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[3], '/bin/bash', '-c', 'echo \"network.host: 172.17.0.5\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.ES_NODES[3], '/bin/bash', '-c', 'echo \"discovery.zen.ping.unicast.hosts: ["172.17.0.2", "172.17.0.3", "172.17.0.4", "172.17.0.5", "172.17.0.6"]\" >> /etc/elasticsearch/elasticsearch.yml'])
print("[ELASTICSEARCH] Configure elasticsearch.yml for kibana")
subprocess.run(['docker', 'exec', "-t", "-d", config.KIBANA_NODES[0], '/bin/bash', '-c', 'echo \"node.name: kibana\" > /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.KIBANA_NODES[0], '/bin/bash', '-c', 'echo \"cluster.name: mycluster\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.KIBANA_NODES[0], '/bin/bash', '-c', 'echo \"http.port: 9200\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.KIBANA_NODES[0], '/bin/bash', '-c', 'echo \"node.master: false\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.KIBANA_NODES[0], '/bin/bash', '-c', 'echo \"node.data: true\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.KIBANA_NODES[0], '/bin/bash', '-c', 'echo \"network.host: 172.17.0.6\" >> /etc/elasticsearch/elasticsearch.yml'])
subprocess.run(['docker', 'exec', "-t", "-d", config.KIBANA_NODES[0], '/bin/bash', '-c', 'echo \"discovery.zen.ping.unicast.hosts: ["172.17.0.2", "172.17.0.3", "172.17.0.4", "172.17.0.5", "172.17.0.6"]\" >> /etc/elasticsearch/elasticsearch.yml'])

for node in config.ES_NODES:
    runcmd(node, config.ES_BIN_PATH, 'restart')
for node in config.KIBANA_NODES:
    runcmd(node, config.KIBANA_BIN_PATH, 'restart')


subprocess.run(['docker', 'exec', '-t', '-d', 'config.ES_NODES[0]', 'usr/share/elasticsearch/cerebro/bin/cerebro'])

#subprocess.run(['docker', 'exec', "-t", '-d', 'elk0', 'service', 'elasticsearch', 'start'])
#subprocess.run(['docker', 'exec', "-t", '-d', 'elk1', '/bin/bash', '-c', '/etc/init.d/elasticsearch', 'stop'])
#subprocess.run(['docker', 'exec', 'elk1', '/bin/bash', '-c', '/etc/init.d/elasticsearch', 'restart'])
#subprocess.run(['docker', 'exec', "-t", 'elk2', '/etc/init.d/elasticsearch', 'start'])
#subprocess.run(['docker', 'exec', "-t", 'elk3', '/etc/init.d/elasticsearch', 'start'])
#subprocess.run(['docker', 'exec', "-t", 'elk4', '/etc/init.d/elasticsearch', 'start'])

print(str(datetime.datetime.now()) + " Completed")

print("\n--- %s seconds ---" % (time.clock() - start_time))
