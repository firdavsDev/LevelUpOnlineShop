## Django commands

### Install Django
```bash
pip install django
```

### Create a new Django project
```bash
django-admin startproject config .
```

### Run the Django server
```bash
python manage.py runserver
```

### Save changes to the Database
```bash
python manage.py migrate
```

### Create superuser
```bash
python manage.py createsuperuser
```

### Create a new app
```bash
python manage.py startapp app_name

# add app_name to INSTALLED_APPS in settings.py

```

### Change the database
```bash
python manage.py makemigrations
```

### Apply changes to the database
```bash
python manage.py migrate
```