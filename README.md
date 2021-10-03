# Doc
+ https://www.tutorialspoint.com/django/django_creating_views.htm

# Install
 + pip install django
 + install for database: pip install mysqlclient
 


# Create project
  + Django-admin startproject ecourses
  + Create app on project: django-admin startapp courses
  + Code first: 
    + python manage.py makemigrations courses
    + python manage.py sqlmigrate courses ten_file
    + python manage.py migrate
# Run project
 + Run local: python manage.py runserver //default port: 8000
 
# Some syntax on shell
 + from courses.models import *
 + Create new record in Category
   + Th1
   + c = Category(name="Lap trinh java)
   + c.save()
   + Th2
   + c = Category.object.create(name="Lap trinh java)
   + Th3
   + c = Category.object.get_or_create(name="Lap trinh java)
   
 + Get
   + c = Category.object.get(pk=1)
 