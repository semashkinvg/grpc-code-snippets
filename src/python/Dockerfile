FROM python:3.10-buster as build

EXPOSE 50051

RUN apt-get -y update && apt-get -y install python3 python3-pip --no-install-recommends

COPY src/python/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/python/server /app

COPY /protos /protos

RUN /protos/generate.sh /app
WORKDIR /app
CMD ["python3", "./server.py"]