FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN apk add libffi-dev
RUN python3 -m pip install --upgrade pip
RUN pip install -r /requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

RUN mkdir /store
WORKDIR /store
COPY . .