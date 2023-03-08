TAG=$1

docker tag random-web:latest panda1024/random-web:${TAG}
docker push panda1024/random-web:${TAG}