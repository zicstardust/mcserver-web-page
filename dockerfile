FROM python:3.13.6-alpine

ENV PYTHONUNBUFFERED=1
ENV UID=1000
ENV GID=1000

WORKDIR /app

COPY requirements.txt .
COPY /app .

RUN apk add --no-cache su-exec shadow; \
    addgroup mcwebserver -g ${GID}; \
    adduser -D -u ${UID} -G mcwebserver mcwebserver; \
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
