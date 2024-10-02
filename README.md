# Firmsnap Enterprise Wiki

## Deployment details
 - Run `$ python manage.py tailwind built` to use django-tailwind to build the styles.css inside theme/static/css/dist

 - Run `$ python manage.py collectstatic` to populate /staticfiles/ directory. These files will be served by nginx.

 - Run `$ eb deploy && eb open` to deploy to Elastic Beanstalk and open the homepage.
     