#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Create superuser if environment variable is set
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi