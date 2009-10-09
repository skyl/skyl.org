This app is tested with my branch of pinax that stays merged with pinax head

    git clone git://github.com/skyl/pinax.git  

or you can make your own branch.  Pinax trunk will probably work 
(well, you need django-events and django-listings that aren't in the
requirements file so no).  You can modify the instructions found here:

    http://pinaxproject.com/docs/dev/contributing.html

This project uses Django 1.1 or trunk but django-events does not work with <1.1

    pip install -U django


