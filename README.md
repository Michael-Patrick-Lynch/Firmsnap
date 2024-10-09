# Firmsnap Enterprise Forum

## Deployment details
 - Run `$ python manage.py tailwind build` to use django-tailwind to build the styles.css inside theme/static/css/dist

 - Run `$ python manage.py collectstatic` to populate /staticfiles/ directory. These files will be served by nginx.

 - Run `$ eb deploy && eb open` to deploy to Elastic Beanstalk and open the homepage.

## Local development

 - Run `$ python manage.py tailwind start` to have Tailwind assets build automatically when you change them

 - Run `$ python manage.py runserver` to run dev server

## Notes

 - If you ever see Django + Tailwind = heart show up on the screen, that means you are rendering from 'base.html' not 'app/base.html'