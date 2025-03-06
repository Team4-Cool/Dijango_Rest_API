from .base import *

# Dummy value for development
SECRET_KEY = 'django-insecure-_17nl5nig(w$k7*cx26xu)8*t3+*09p0fj7inm+honh0k1k22p'

DEBUG_TOOLBAR = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'TaskBoard',  # Replace with your database name
        'USER': 'postgres',  # Replace with your database username
        'PASSWORD': 'admin1234',  # Replace with your database password
        'HOST': 'localhost',  # Or the IP address of the server hosting the database
        'PORT': '5432',  # Default PostgreSQL port
    }
}

if DEBUG_TOOLBAR:
    # Add django extensions
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

    # Configure django-debug-toolbar
    DEBUG_TOOLBAR_PANELS = [
        "ddt_request_history.panels.request_history.RequestHistoryPanel",
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ]

    # Needed for django-debug-toolbar
    INTERNAL_IPS = [
        "109.87.215.193",
    ]

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)