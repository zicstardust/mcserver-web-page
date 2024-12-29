FROM python:3.13.1-slim

ENV PYTHONUNBUFFERED=1

ENV PORT=5000
ENV UID=1001
ENV GID=1001

WORKDIR /app

COPY . .

RUN groupadd -g ${GID} mcwebserver; \
    useradd mcwebserver -u ${UID} -g mcwebserver; \
    pip3 install --no-cache-dir -r requirements-prod.txt; \
    echo '#!/bin/sh' > /app/start.sh; \
    echo 'waitress-serve --port=${PORT} --call main:production' >> /app/start.sh; \
    chown -R mcwebserver:mcwebserver /app; \
    chmod 775 /app/start.sh

EXPOSE ${PORT}

USER mcwebserver
CMD [ "/app/start.sh" ]
