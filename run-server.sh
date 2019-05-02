#!/bin/sh
.env/bin/python manage.py migrate
.env/bin/python manage.py runserver 0.0.0.0:${PORT:-'8000'}