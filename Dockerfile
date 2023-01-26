FROM ubuntu:20.04

MAINTAINER Spashev Nurken

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONFAULTHANDLER 1
ENV PYTHONBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add alpine mirrors
RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get install -y tzdata \
  && apt-get install -y python3.11 python3-pip \
  && apt-get install -y --no-install-recommends python3-dev \
  && apt-get install -y --no-install-recommends nginx \
  && apt-get install -y --no-install-recommends libpq-dev \
  && apt-get install -y --no-install-recommends apt-utils \
  && apt-get install -y --no-install-recommends libc-dev \
  && apt-get install -y --no-install-recommends gcc \
  && apt-get install -y --no-install-recommends gettext \
  && apt-get install -y --no-install-recommends screen \
  && apt-get clean


# Set python requirements
WORKDIR /code

# Install python dependencies

COPY src/app /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt \
    && pip install Redis \
    && pip install uvicorn  \
    && pip install psycopg2 \
    && pip install flake8 \
    && pip install pytest-django

EXPOSE 8010

COPY docker/start.uvicorn.sh ./
RUN chmod +x ./start.uvicorn.sh
