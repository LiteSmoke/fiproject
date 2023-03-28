from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from fi import urls


urlpatterns = [
    path('', include('fi.urls')),
    path('admin/', admin.site.urls),
    path('api/', get_schema_view(
        title="FI project",
        description="API for FI project",
        version="0.0.1"
    ), name="openapi-schema"),
    path('swagger/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
]
