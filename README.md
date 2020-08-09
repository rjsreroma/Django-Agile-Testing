# Local environment
pip install pipenv <br />
pipenv shell

# Github cloning
git clone https://github.com/rjsreroma/django-agile-testing.git


# Migrate database since I was using SQLite

python manage.py makemigrations values_principles <br />
python manage.py migrate values_principles


# For testing API and models

pytest

# For running the API
python manage.py runserver
