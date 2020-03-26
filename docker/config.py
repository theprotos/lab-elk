DOCKERFILE_OPENJDK = "config/Dockerfile-openjdk"
DOCKERFILE_KIBANA = "config/Dockerfile-kibana"
DOCKERFILE_ORACLEJDK = "config/Dockerfile-oraclejava"
DOCKERFILE_ES = "config/Dockerfile-es"

DOCKERIMAGE_OPENJDK = "docker:openjdk"
DOCKERIMAGE_KIBANA = "docker:kibana"
DOCKERIMAGE_ORACLEJDK = "docker:oraclejdk"
DOCKERIMAGE_ES = "docker:es"

ES_NODES = ["es1", "es2", "es3", "es4"]
KIBANA_NODES = ["kib1", "kib2"]

HTTP_PYTHON = "python -m SimpleHTTPServer 8000"
ES_BIN_PATH = "/etc/init.d/elasticsearch"
KIBANA_BIN_PATH = "/etc/init.d/kibana"
