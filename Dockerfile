FROM oneoffcoder/python-java:latest

LABEL author="Jee Vang, Ph.D."
LABEL email="vangjee@gmail.com"

ARG AAPI_VERSION
ARG APYPI_REPO

ENV API_VERSION=$AAPI_VERSION
ENV PYPI_REPO=$APYPI_REPO

RUN apt-get update \
    && apt-get upgrade -y
COPY . /code
RUN pip install -r /code/requirements.txt
RUN /code/publish.sh