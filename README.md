# recipe-app-api
Receipe App Api source code

- docker-compose run --rm app sh -c "python manage.py createsuperuser"  
- docker-compose run --rm app sh -c "python manage.py startapp core"       
- docker-compose run --rm app sh -c "python manage.py makemigrations"
- docker-compose run --rm app sh -c "python manage.py migrate"
- docker-compose run --rm app sh -c "python manage.py test && flake8"
