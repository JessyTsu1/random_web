TAG=${1:-latest}

docker build -t random-web:$TAG  -f ./docker/Dockerfile .