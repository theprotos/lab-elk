#!/bin/bash

. ../config/profile.cfg

echo  "Install plugins"
for plugin in "${pluginsInstall[@]}"
do
    echo "Install ${plugin}"
    #TODO: env in quotes doesn work
    #curl -X POST \
    #-d '<jenkins><install plugin="\"$plugin@latest"\" /></jenkins>' \
    #--header 'Content-Type: text/xml' ${jenkinsHostURL}'/pluginManager/installNecessaryPlugins'
    #TODO: env in quotes doesn work, the same
    #curl -XPOST ${jenkinsHostURL}/pluginManager/installNecessaryPlugins -d '<install plugin="\"$plugin@latest"\" />'
done
#TODO: move to loop above
#curl -XPOST ${jenkinsHostURL}/pluginManager/installNecessaryPlugins -d '<install plugin="greenballs@latest" />'
curl -X POST -d '<jenkins><install plugin="greenballs@latest" /></jenkins>' --header 'Content-Type: text/xml' ${jenkinsHostURL}${jenkinsPluginPath}
#curl -X POST ${jenkinsHostURL}${jenkinsPluginPath} -d '<install plugin="git@latest" />'
#curl -X POST ${jenkinsHostURL}${jenkinsPluginPath} -d '<install plugin="job-dsl@latest" />'
#curl -X POST ${jenkinsHostURL}${jenkinsPluginPath} -d '<install plugin="ant@latest" />'
#curl -X POST ${jenkinsHostURL}${jenkinsPluginPath} -d '<install plugin="maven-plugin@latest" />'
#curl -X POST ${jenkinsHostURL}${jenkinsPluginPath} -d '<install plugin="monitoring@latest" />'
sleep 30
#curl -X POST "${jenkinsHostURL}/safeRestart"
curl -X POST "${jenkinsHostURL}/Restart"
