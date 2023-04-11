FROM python:3.10-buster as build
LABEL org.opencontainers.image.source="https://github.com/semashkinvg/grpc-python-server"

EXPOSE 50051

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install \
        python3=3.7.3-1 \
        python3-pip=18.1-5 --no-install-recommends \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /
COPY src/python/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/python/server /app

COPY /protos /protos

RUN /protos/generate.sh /app
WORKDIR /app
CMD ["python3", "./server.py"]