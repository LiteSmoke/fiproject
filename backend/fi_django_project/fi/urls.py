from rest_framework.routers import DefaultRouter
from django.urls import path, include
from fi.views import UserViewSet

app_name = 'fi'

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]