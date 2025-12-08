python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn VoterIdCard.wsgi:application --bind 0.0.0.0:$PORT