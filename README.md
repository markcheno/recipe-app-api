# recipe-app-api

Receipe App Api source code

- docker-compose run --rm app sh -c "python manage.py createsuperuser"
- docker-compose run --rm app sh -c "python manage.py startapp core"
- docker-compose run --rm app sh -c "python manage.py makemigrations"
- docker-compose run --rm app sh -c "python manage.py migrate"
- docker-compose run --rm app sh -c "python manage.py test && flake8"
- docker-compose run --rm -e PGPASSWORD=supersecretpassword app sh -c "pg_dumpall -h db -U postgres | gzip -9 > backup.sql.gz"
