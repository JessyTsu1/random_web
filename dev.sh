TAG=${1:-latest}

docker run --rm -it \
    -p 5000:5000 \
    -v /etc/localtime:/etc/localtime:ro \
    -v "$PWD/src":"/opt/random-web" \
     random-web:$TAG \
     conda run --no-capture-output --name random-web python3 app.py -d -vv