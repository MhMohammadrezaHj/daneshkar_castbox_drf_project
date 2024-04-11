"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version="1.0.0",
        description="API documentation of App",
    ),
    public=True,
)

# from rest_framework_swagger.views import get_swagger_view

admin_endpoint = "admin"
# schema_view = get_swagger_view(title="Pastebin API")

urlpatterns = [
    # swagger
    # path("xss/", schema_view),
    path(f"{admin_endpoint}/", admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                path("auth/", include("djoser.urls")),
                path("auth/", include("djoser.urls.jwt")),
                path("", include("contents.urls")),
                path("my/", include("activites.urls")),
                path("log/", include("logs.urls")),
                path(
                    "swagger/schema/",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="swagger-chema",
                ),
            ]
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
