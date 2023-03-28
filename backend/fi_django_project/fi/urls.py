from rest_framework.routers import DefaultRouter
from django.urls import path, include
from fi.views import (
    UserViewSet,
    TransactionViewSet,
    TransactionCategoryViewSet,
)

app_name = 'fi'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'transaction-category', TransactionCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]