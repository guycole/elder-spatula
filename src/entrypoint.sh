#!/bin/bash
#
# Title:entrypoint.sh
# Description: 
# Development Environment: debian 11 bullseye
#
RUN_PORT="8000"
#
/usr/bin/python3 django/manage.py migrate --no-input
#
cd /app/django
/usr/local/bin/gunicorn spatula.wsgi:application --bind "0.0.0.0:${RUN_PORT}" --daemon
#
/usr/sbin/nginx -g 'daemon off;'
#