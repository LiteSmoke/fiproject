from rest_framework.serializers import HyperlinkedModelSerializer
from fi.models import User


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'email', 'username']