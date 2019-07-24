from django.urls import path
from .views import *
from .ajax import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'flat', FlatViewSet)
router.register(r'flatmate', FlatmateViewSet)
router.register(r'room', RoomViewSet)
router.register(r'cleanup', CleanUpViewSet)
router.register(r'record', RecordViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('load-clean/', load_clean, name='load-clean'),
    path('load-points/', load_points, name='load-points'),
    path('load-rooms/', load_rooms, name='load-rooms'),
    path('load-flatmate/', load_flatmate, name='load-flatmate'),

]
