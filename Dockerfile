FROM python:latest
MAINTAINER yunwei@ruitone.com.cn
ADD . /python
RUN pip3 install -r /python/requirements.txt
WORKDIR /python
CMD ["python", "run.py"]