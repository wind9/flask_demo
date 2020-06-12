FROM python:latest
MAINTAINER yunwei@ruitone.com.cn
ADD . /python
RUN pip3 install -r /python/requirements.txt
WORKDIR /python
EXPOSE 8080
CMD ["python", "run.py"]