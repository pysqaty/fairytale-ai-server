#!/bin/bash
set -e

# Collect static files
# python manage.py collectstatic --no-input

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
# if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] && [ "$DJANGO_SUPERUSER_EMAIL" ]; then
#     python manage.py createsuperuser --no-input || true
# fi

# Start the server
exec "$@"