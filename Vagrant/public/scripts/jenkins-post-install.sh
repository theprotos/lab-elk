#!/bin/bash

. ../config/profile.cfg

echo "Add to sudoers"
sudo sh -c "echo \"jenkins ALL=(ALL) NOPASSWD: /var/lib/jenkins/*, /usr/bin/*, /var/lib/tomcat/build/bin/*, /var/lib/tomcat/bin/*\" >> /etc/sudoers"
sleep 20
echo "Required for SLAVES/REMOTE API"
curl -X POST \
-d 'json=%7B%22useSecurity%22%3A+%7B%22slaveAgentPort%22%3A+%7B%22type%22%3A+%22fixed%22%2C+%22value%22%3A+%2250000%22%7D%7D%2C+%22core%3Aapply%22%3A+%22true%22%7D' \
--header 'Content-Type: application/x-www-form-urlencoded' ${jenkinsHostURL}/configureSecurity/configure
sleep 20

#TODO: build xml with xmlstarlet
#sudo xmlstarlet ed -i /hudson/jdks -t elem -n jdk -v "" /var/lib/jenkins/config-copy.xml
echo "Copy jenkins config"
sudo cp ../config/config.xml /var/lib/jenkins
curl -X POST "${jenkinsHostURL}/safeRestart"
sleep 20
