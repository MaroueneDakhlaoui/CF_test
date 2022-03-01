web: gunicorn coffee.coffee.wsgi
release: python coffee/manage.py makemigrations --input
release: python coffee/manage.py collectstatic --noinput
release: python coffee/manage.py migrate --noinput