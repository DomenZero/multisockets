# set base image (host OS)
FROM python:3.8-alpine as builder

# set the working directory in the container
WORKDIR /

COPY server_code.py .
COPY results.txt .

# install dependencies
RUN apk add --no-cache python3-dev \
                       build-base \
                       libc6-compat \
                       libffi-dev \
                       zlib-dev \
                       jpeg-dev \
                       linux-headers
RUN pip3 install --upgrade pip
# RUN pip install -r requirements.txt

EXPOSE 9005
# command to run on container start
CMD [ "python", "server_code.py" ]
