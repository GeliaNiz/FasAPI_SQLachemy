FROM python:latest
MAINTAINER Nizamutdinova Angelina 'angelinanizam@gmail.com'
WORKDIR /usr/src/app
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 8000

