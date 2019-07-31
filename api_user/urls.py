from .views import CustomUserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', CustomUserViewSet)
