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
    path('flatmate/', FlatmateList.as_view(), name='flatmate-list'),
    path('flatmate/<int:pk>/', FlatmateDetail.as_view(), name='flatmate-detail'),
    path('room/', RoomList.as_view(), name='room-list'),
    path('room/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
    path('cleanup/', CleanUpList.as_view(), name='cleanup-list'),
    path('cleanup/<int:pk>/', CleanUpDetail.as_view(), name='cleanup-detail'),
    path('record/', RecordList.as_view(), name='record-list'),
    path('record/<int:pk>/', RecordDetail.as_view(), name='record-detail'),
]
