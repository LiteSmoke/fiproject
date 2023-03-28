from rest_framework.viewsets import ModelViewSet
from fi.models import (
    User,
    Transaction,
    TransactionCategory,
)
from fi.serializers import (
    UserSerializer,
    TransactionSerializer,
    TransactionCategorySerializer,
)


class UserViewSet(ModelViewSet):
    """User view set to manage User API"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransactionViewSet(ModelViewSet):
    """Transaction view set for API"""

    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer


class TransactionCategoryViewSet(ModelViewSet):
    """Transaction category view set for API"""

    queryset = TransactionCategory.objects.all()
    serializer_class = TransactionCategorySerializer
