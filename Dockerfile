FROM python:3.11.1

MAINTAINER "jiaoyuan@testbird.com"

ARG PROJECT_NAME=django_cas_server

WORKDIR /data/$PROJECT_NAME/

COPY requirements.txt ./

RUN apt update && apt install -y gcc g++ make git python3-dev libmariadb-dev musl-dev libffi-dev \
    libjpeg-dev zlib1g-dev libxml2-dev libxslt-dev

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
ENTRYPOINT ["bash", "start.sh"]
CMD ["bash", "/data/$PROJECT_NAME/start.sh"