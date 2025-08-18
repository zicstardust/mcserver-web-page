#!/bin/sh
set -e

if [ "$(id -g mcwebserver)" != "${PGID}" ]; then
    groupmod -o -g "${PGID}" mcwebserver
fi


if [ "$(id -u mcwebserver)" != "${PUID}" ]; then
    usermod -o -u "${PUID}" mcwebserver
fi

mkdir -p /data 
chown -R mcwebserver:mcwebserver /home/mcwebserver /data /app

exec su-exec mcwebserver "$@"
