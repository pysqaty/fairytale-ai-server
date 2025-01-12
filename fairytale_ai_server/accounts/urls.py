from accounts.api import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users-viewset')

urlpatterns = router.urls
