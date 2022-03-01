web: gunicorn coffeeproject/coffee/wsgi.py
release: python coffeeproject/manage.py makemigrations --input
release: python coffeeproject/manage.py collectstatic --noinput
release: python coffeeproject/manage.py migrate --noinput