web: gunicorn coffee.coffee.wsgi
release: python manage.py makemigrations --input
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput