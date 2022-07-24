#!/bin/bash
source venv/bin/activate

echo $REDIS_URL

celery worker -A celery_worker.celery --loglevel=info