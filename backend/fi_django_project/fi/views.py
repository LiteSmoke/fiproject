from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

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

    # @csrf_exempt
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        """Permanently deletes all transactions"""

        count = Transaction.objects.all().delete()[0]
        return Response({"message":f"{count} transactions deleted."}, status=status.HTTP_204_NO_CONTENT)


class TransactionCategoryViewSet(ModelViewSet):
    """Transaction category view set for API"""

    queryset = TransactionCategory.objects.all()
    serializer_class = TransactionCategorySerializer
