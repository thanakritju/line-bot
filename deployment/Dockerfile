FROM python:3.7-alpine

MAINTAINER Thanakrit Gwan Juthamongkhon (thanakrit.ju.work@gmail.com)

WORKDIR /home

ADD deployment/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD app app

CMD ["python", "app/main.py"]
