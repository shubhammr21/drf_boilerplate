from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/api/', include_docs_urls(title="Grampower SSO Auth Server")),
    path('api/dlms/', include("dlms.urls")),
]

if "drf_yasg" in settings.INSTALLED_APPS:
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    from rest_framework import permissions
    schema_view = get_schema_view(
        openapi.Info(
            title="MDAS",
            default_version='dev',
            description="""

This is a Development Documentation [MDAS](/).
To interact with api's links, expand the link and click 'Try it out'
The `basic-ui` view can be found [here](/docs/api/).
The `swagger-ui` view can be found [here](/docs/swagger).
The `redoc-ui` view can be found [here](/docs/redoc/).
to authenticate: Post /user/auth/login with username and password then you will get an token\n
goto authorize button and enter 'token YOUR_KEY' in input box. then hit authorize.""",  # noqa

            contact=openapi.Contact(
                email="shubhammaurya@grampower.com"
            ),
        ),
        public=True,
        permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
    )
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path(
            'docs/swagger/',
            schema_view.with_ui(
                'swagger',
                cache_timeout=0
            ),
            name='schema-swagger-ui'
        ),
        path(
            'docs/redoc/',
            schema_view.with_ui(
                'redoc',
                cache_timeout=0
            ),
            name='schema-redoc'
        ),
    ]