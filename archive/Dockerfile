FROM python:3.7-alpine

RUN apk update \
&& apk upgrade \
&& apk add --no-cache bash \
&& apk add --no-cache --virtual=build-dependencies unzip \
&& apk add --no-cache curl \
&& apk add --no-cache openjdk8-jre

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz && tar -xzf geckodriver-v0.26.0-linux64.tar.gz && rm geckodriver-v0.26.0-linux64.tar.gz
RUN mv geckodriver usr/local/bin/geckodriver

COPY src/driver.py driver.py
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV AWS_USER=$AWS_USER
ENV AWS_PASSWORD=$AWS_PASSWORD
ENV AWS_ADMIN=$AWS_ADMIN

ENTRYPOINT ["/bin/sh"]
#ENTRYPOINT ["python", "driver.py"]