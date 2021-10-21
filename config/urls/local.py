from .base import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
