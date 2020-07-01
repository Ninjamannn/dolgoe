FROM python:3.7-alpine AS base


RUN adduser -D dolgoe
WORKDIR /home/dolgoe

ENV FLASK_APP bjoern_dolgoe.wsgi:bjoern.run
ENV FLASK_CONFIGURATION DEV
ENV PYTHONUNBUFFERED 0                    # for normal log

EXPOSE 2020

FROM base AS dependencies

ADD requirements.txt .

RUN apk add --no-cache htop && \
    apk add --no-cache bash && \
    apk add --no-cache nano && \
    apk add --no-cache libev-dev && \
    apk add --update postgresql-libs && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev && \
    apk add --update  --no-cache libstdc++ libc6-compat openssh-client git gcc cython linux-headers make musl-dev python3-dev g++ && \
    rm -r -f /var/cache/apk/* && \
    python -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements.txt --no-cache-dir && \
    venv/bin/pip install gunicorn --no-cache-dir && \
    apk --purge del .build-deps

FROM dependencies AS build

COPY . .

RUN chmod +x boot.sh && \
    chown -R dolgoe:dolgoe ./

USER dolgoe

ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE

CMD ./boot.sh
