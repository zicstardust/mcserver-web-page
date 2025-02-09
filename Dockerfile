FROM python:3.13.2-alpine

ENV PYTHONUNBUFFERED=1

ENV PORT=5000
ENV UID=1000
ENV GID=1000

WORKDIR /home/mcwebserver

COPY requirements.txt .
COPY /app .

RUN addgroup mcwebserver -g ${GID}; \
    adduser mcwebserver -u ${UID} -D -G mcwebserver; \
    mkdir -p /data; \
    chown -R mcwebserver:mcwebserver /data; \
    chown -R mcwebserver:mcwebserver /home/mcwebserver
    
USER mcwebserver

RUN pip3 install --user --no-cache-dir -r requirements.txt; \
    ln -s /data /home/mcwebserver/data; \
    echo '#!/bin/sh' > /home/mcwebserver/start.sh; \
    echo 'waitress-serve --port=${PORT} --call main:production' >> /home/mcwebserver/start.sh; \
    chmod 775 /home/mcwebserver/start.sh

ENV PATH="/home/mcwebserver/.local/bin:${PATH}"

EXPOSE ${PORT}

CMD [ "/home/mcwebserver/start.sh" ]
