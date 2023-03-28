from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from fi.models import (
    User,
    Transaction,
    TransactionCategory,
)


class UserSerializer(HyperlinkedModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = ['url', 'email', 'username']


class TransactionSerializer(ModelSerializer):
    """Transaction serializer"""

    class Meta:
        model = Transaction
        fields = ['date', 'type', 'amount', 'description', 'category']


class TransactionCategorySerializer(ModelSerializer):
    """Transaction category serializer"""

    class Meta:
        model = TransactionCategory
        fields = ['name', 'parent']