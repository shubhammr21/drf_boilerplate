from .base import *

ALLOWED_HOSTS += ["localhost", "0.0.0.0", "127.0.0.1"]
INSTALLED_APPS.append("django_extensions")  # noqa F405
INSTALLED_APPS.append("debug_toolbar")  # noqa: F405

MIDDLEWARE.insert(  # noqa: F405
    3, "debug_toolbar.middleware.DebugToolbarMiddleware"
)

ROOT_URLCONF = "config.urls.local"
def show_toolbar(request):
    """Use env variable to decide when to show debug tooolbar"""
    return env.bool(  # noqa: F405
        "SHOW_DEBUG_TOOLBAR", default=DEBUG
    )


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar
}

# Celery
# ------------------------------------------------------------------------------

# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True
