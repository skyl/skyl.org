#!/bin/bash

PROJECT_ROOT=/home/skyl/proj/skyl

# activate virtual environment
source /home/skyl/mypinax/pinax-dev/bin/activate

cd /home/skyl/proj/skyl
python manage.py send_mail >> $PROJECT_ROOT/logs/cron_mail.log 2>&1
python manage.py emit_notices
python manage.py retry_deferred
