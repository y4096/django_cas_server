#!/usr/bin/env bash

project=django_cas_server
ver=$1
ver=${ver:-"0.0.1"}
echo "will deploy ver: $ver"
echo "1.prod  2.stage"
read -r -p "select environment: " env
case $env in
  1)
    env=prod;;
  2)
    env=stage;;
  *)
    echo "error input"
    exit
esac

#sudo docker stop ${project}_${env} 2>/dev/null
#sudo docker rm -f ${project}_${env} 2>/dev/null
#echo "remove image"
#sudo docker rmi tbgd/${project}_${env}:${ver}
sudo docker build . -t tbgd/${project}_${env}:${ver}
#sudo docker push tbgd/${project}_${env}:${ver}
#sudo docker pull tbgd/${project}_${env}:${ver}
sudo docker stop ${project}_${env} 2>/dev/null
sudo docker rm -f ${project}_${env} 2>/dev/null

sudo docker run -itd --name ${project}_${env} --net host --env site_env=${env} \
  -v /data/${project}_docker_shard/${env}/assets:/data/${project}/assets \
  -v /data/${project}_docker_shard/${env}/logs:/data/${project}/logs \
  -v /data/${project}_docker_shard/${env}/prometheus:/data/${project}/prometheus \
  --restart always tbgd/"${project}_${env}:${ver}"
