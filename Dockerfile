FROM python:3.7-slim-buster

ENV PYTHONIOENCODING UTF-8
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get update && \
    apt-get install -y \
        make \
        curl

COPY . /app

WORKDIR /app

# update to avoid 'setup.py' not found error
# RUN pip3 install -U pip
RUN pip3 install .

RUN rm -rf /var/lib/apt/lists/*

CMD [ "make", "launch" ]