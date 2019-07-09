from django.shortcuts import render
from .models import Room, Flat, Flatmate, Record, Clean
# Create your views here.


def load_clean(request):
    room = request.GET.get('room')
    r = Room.objects.get(name=room)
    cleans = Clean.objects.filter(room=r)
    return render(request, '../templates/admin/api/record/dropdown.html', {'cleans': cleans})


def load_points(request):
    name = request.GET.get('clean')
    room = request.GET.get('room')
    r = Room.objects.get(name=room)
    clean = Clean.objects.filter(room=r).get(name=name)
    return render(request, '../templates/admin/api/record/points.html', {'clean': clean})
