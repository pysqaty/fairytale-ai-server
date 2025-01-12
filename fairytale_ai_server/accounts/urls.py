from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.api import UserViewSet, UserAuthViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users-viewset')
router.register(r'auth', UserAuthViewSet, basename='user-auth')

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls

