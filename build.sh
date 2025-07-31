#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py build_static_bundle