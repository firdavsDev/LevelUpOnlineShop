#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
python manage.py runserver
