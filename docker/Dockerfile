FROM continuumio/miniconda3:4.10.3-alpine

WORKDIR /opt/random-web

# Need the following line in mainland China
COPY ./docker/tsinghua.condarc /root/.condarc

COPY ./docker/conda_env.yml /opt/random-web/conda_env.yml


RUN conda env create -f conda_env.yml && conda clean -afy
RUN rm -f conda_env.yml

# Need to separate the pip from conda env yaml so we can specify the mirror for mainland China
RUN conda run --no-capture-output --name pku-ece-cv pip install --no-cache-dir urllib3==1.26.8 python-dateutil==2.8.2 openpyxl PyYAML==5.4.1 cos-python-sdk-v5==1.9.15 pytz==2022.05 retry -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./src .

COPY ./docker/config /etc/random-web

ENV NUM_PROCESS=2
ENV NUM_THREAD=2
ENV TIME_OUT=1800


CMD conda run --no-capture-output --name random-web uwsgi \
    --http 0.0.0.0:8088 \
    --uid root \
    --enable-threads \
    --lazy \
    --processes $NUM_PROCESS\
    --threads $NUM_THREAD \
    --logto /var/log/pku-ece-cv.log \
    --protocol uwsgi \
    --http-timeout $TIME_OUT \
    --harakiri $TIME_OUT \
    --wsgi app:app