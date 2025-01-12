from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from accounts.serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer