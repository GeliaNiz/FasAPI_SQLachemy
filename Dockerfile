FROM python:latest
MAINTAINER Nizamutdinova Angelina 'angelinanizam@gmail.com'
WORKDIR /phonebook_app
COPY ./ /phonebook_app
RUN pip install -r requirements.txt
EXPOSE 8000

