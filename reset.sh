# Remove migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Remove database
rm db.sqlite3

# Create new migrations
python manage.py makemigrations

# Create database
python manage.py migrate

# Create superuser
DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_EMAIL=j@kob.dk \
DJANGO_SUPERUSER_PASSWORD=Abc12345 \
python manage.py createsuperuser --noinput

# Load test data
python manage.py loaddata clients
python manage.py loaddata technologies
python manage.py loaddata employees
python manage.py loaddata technologylevel
python manage.py loaddata projects

