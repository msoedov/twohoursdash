
APPS = "twohours"

default: _requirements db test run

_requirements:
	@pip install --exists-action=s -r requirements.txt

req: _requirements

db: syncdb migrate loaddata


migrate:
	@python manage.py migrate -v 0

syncdb:
	@python manage.py syncdb --noinput -v 0

loaddata:
	@python manage.py stub

run:
	@python manage.py runserver

test:
	@python manage.py test $(APPS)

