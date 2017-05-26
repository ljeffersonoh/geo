# FROM continuumio/anaconda3:4.3.1
FROM python:3
# FROM kaggle/python

WORKDIR /app

RUN pip install Pyrebase==3.0.27

# RUN mkdir -p /tmp
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install -e .

