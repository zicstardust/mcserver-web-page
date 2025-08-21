FROM python:3.13.7-alpine

ENV PYTHONUNBUFFERED=1
ENV PUID=1000
ENV PGID=1000

WORKDIR /app

COPY requirements.txt .
COPY /app .

RUN apk add --no-cache su-exec shadow; \
    addgroup mcwebserver -g ${PGID}; \
    adduser -D -u ${PUID} -G mcwebserver mcwebserver; \
    mkdir -p /home/mcwebserver; \
    chown -R mcwebserver:mcwebserver /home/mcwebserver; \
    su-exec mcwebserver pip3 install --user --no-cache-dir -r requirements.txt; \
    ln -s /data /app/data

ENV PATH="/home/mcwebserver/.local/bin:${PATH}"

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["waitress-serve", "--port=5000", "--call", "main:production"]
