#!/bin/sh
set -e

if [ "$(id -g mcwebserver)" != "${GID}" ]; then
    groupmod -o -g "${GID}" mcwebserver
fi


if [ "$(id -u mcwebserver)" != "${UID}" ]; then
    usermod -o -u "${UID}" mcwebserver
fi

mkdir -p /data 
chown -R mcwebserver:mcwebserver /home/mcwebserver /data /app

exec su-exec mcwebserver "$@"
