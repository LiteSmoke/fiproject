from rest_framework.viewsets import ModelViewSet
from fi.models import User
from fi.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """User view set to manage User API"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
