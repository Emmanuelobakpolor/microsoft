#!/bin/bash

# Startup script for Azure App Service

# Run Django migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start gunicorn
gunicorn config.wsgi:application --bind=0.0.0.0:8000 --workers=4 --worker-class=sync
