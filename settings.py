# -*- coding: utf-8 -*-
# Django settings for complete pinax project.

import os.path
import pinax

PINAX_ROOT = os.path.realpath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

# tells Pinax to use the default theme
PINAX_THEME = 'default'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through django.views.static.serve.
SERVE_MEDIA = DEBUG

ADMINS = (
    ('Skylar Saveland', 'skylar.saveland@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'
from local_settings import DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media")

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/site_media/'


# bsolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'site_media')

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = '/site_media/'
STATICFILES_DIRS = (
            ('skyl', os.path.join(PROJECT_ROOT, 'media')),
            ('pinax', os.path.join(PINAX_ROOT, 'media', PINAX_THEME)),
)


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_openid.consumer.SessionConsumer',
    'account.middleware.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django_sorting.middleware.SortingMiddleware',
    'djangodblog.middleware.DBLogMiddleware',
    'pinax.middleware.security.HideSensistiveFieldsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",

    #"pinax.core.context_processors.contact_email",
    #"pinax.core.context_processors.site_name",
    "pinax.core.context_processors.pinax_settings",

    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",
    "account.context_processors.openid",
    "account.context_processors.account",
    "messages.context_processors.inbox",
    "friends_app.context_processors.invitations",
    "context_processors.combined_inbox_count",
)

COMBINED_INBOX_COUNT_SOURCES = (
    "messages.context_processors.inbox",
    "friends_app.context_processors.invitations",
    "notification.context_processors.notification",
)

INSTALLED_APPS = (
    # included
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.admindocs',
    'pinax.templatetags',
    
    # external
    'notification', # must be first
    'django_openid',
    'emailconfirmation',
    'django_extensions',
    'robots',
    'friends',
    'mailer',
    'messages',
    'announcements',
    'oembed',
    'djangodblog',
    'pagination',
    'gravatar',
    'threadedcomments',
    'threadedcomments_extras',
    'wiki',
    #'swaps',
    'timezones',
    'app_plugins',
    'voting',
    'voting_extras',
    'tagging',
    'bookmarks',
    'blog',
    'ajax_validation',
    'photologue',
    'avatar',
    'flag',
    #'microblogging',
    #'locations',
    'uni_form',
    'django_sorting',
    'django_markup',
    
    # internal (for now)
    'analytics',
    'staticfiles',
    'profiles',
    'account',
    'signup_codes',
    #'tribes',
    
    'projects',
    'tasks',

    'photos',
    'tag_app',
    'topics',
    'groups',
    
    'django.contrib.admin',
    'attachments',
    # Skylar Saveland under implied BSD/Django license
    'events',
    'listings',
    #'geoms'
)

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/profile/%s/" % o.username,
}

MARKUP_FILTER_FALLBACK = 'none'
MARKUP_CHOICES = (
    ('restructuredtext', u'reStructuredText'),
    ('textile', u'Textile'),
    ('markdown', u'Markdown'),
    ('creole', u'Creole'),
)
WIKI_MARKUP_CHOICES = MARKUP_CHOICES

AUTH_PROFILE_MODULE = 'profiles.Profile'
NOTIFICATION_LANGUAGE_MODULE = 'account.Account'

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
CONTACT_EMAIL = "skyl@skyl.org"
SITE_NAME = "skyl.org"
LOGIN_URL = "/account/login/"
LOGIN_REDIRECT_URLNAME = "what_next"

INTERNAL_IPS = (
    '127.0.0.1',
)

ugettext = lambda s: s
LANGUAGES = (
    ('en', u'English'),
)

# URCHIN_ID = "ua-..."

class NullStream(object):
    def write(*args, **kwargs):
        pass
    writeline = write
    writelines = write

RESTRUCTUREDTEXT_FILTER_SETTINGS = {
    'cloak_email_addresses': True,
    'file_insertion_enabled': False,
    'raw_enabled': False,
    'warning_stream': NullStream(),
    'strip_comments': True,
}

# if Django is running behind a proxy, we need to do things like use
# HTTP_X_FORWARDED_FOR instead of REMOTE_ADDR. This setting is used
# to inform apps of this fact
BEHIND_PROXY = False

FORCE_LOWERCASE_TAGS = True

WIKI_REQUIRES_LOGIN = True

# Uncomment this line after signing up for a Yahoo Maps API key at the
# following URL: https://developer.yahoo.com/wsregapp/
# YAHOO_MAPS_API_KEY = ''

AVATAR_DEFAULT_URL = MEDIA_URL + 'avatar.jpg'
AVATAR_GRAVATAR_BACKUP = False

STATICFILES_EXTRA_MEDIA = (
        ('pinax', os.path.join(PINAX_ROOT, 'media', PINAX_THEME)),
        ('SKYL', os.path.join(PROJECT_ROOT, 'media')),
)

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
