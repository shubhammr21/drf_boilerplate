#!/bin/bash

set -o errexit
set -o nounset


rm -f './celerybeat.pid'
celery -A config.celery_app beat -l INFO


celery flower \
    --app=config.celery_app \
    --broker="${CELERY_BROKER_URL}" \
    --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"


watchgod celery.__main__.main --args -A config.celery_app worker -l INFO