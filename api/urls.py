from django.urls import path
from .views import *
from .ajax import *

urlpatterns = [
    path('load-clean/', load_clean, name='load-clean'),
    path('load-points/', load_points, name='load-points'),
    path('load-rooms/', load_rooms, name='load-rooms'),
    path('load-flatmate/', load_flatmate, name='load-flatmate'),
    path('flat/', FlatList.as_view(), name='flat-list'),
    path('flat/<int:pk>/', FlatDetail.as_view(), name='flat-detail'),
]
