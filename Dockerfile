FROM python:3.13.1-alpine

ENV PYTHONUNBUFFERED=1

ENV PORT=5000
ENV UID=1000
ENV GID=1000

WORKDIR /app

COPY requirements.txt .
COPY /app .

RUN addgroup mcwebserver -g ${GID}; \
    adduser mcwebserver -u ${UID} -D -G mcwebserver; \
    pip3 install --no-cache-dir -r requirements.txt; \
    echo '#!/bin/sh' > /app/start.sh; \
    echo 'waitress-serve --port=${PORT} --call main:production' >> /app/start.sh; \
    mkdir -p /data; \
    chown -R mcwebserver:mcwebserver /data; \
    ln -s /data /app/data; \
    chown -R mcwebserver:mcwebserver /app; \
    chmod 775 /app/start.sh

RUN echo '#!/bin/sh' > /run.sh; \
    echo 'chown -R mcwebserver:mcwebserver /data' >> /run.sh; \
    echo 'chmod 700 /data' >> /run.sh; \
    echo 'su -c /app/start.sh mcwebserver' >> /run.sh; \
    chmod 775 /run.sh

EXPOSE ${PORT}

#USER mcwebserver
CMD [ "/run.sh" ]
