from django.urls import path
from .views import *

urlpatterns = [
    path('load-clean/', load_clean, name='load-clean'),
    path('load-points/', load_points, name='load-points'),
]