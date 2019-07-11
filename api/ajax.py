from django.shortcuts import render
from .models import Room, CleanUp, Flat, Flatmate


def load_clean(request):
    room_pk = request.GET.get('room_pk')
    # flat_pk = request.GET.get('flat_pk')
    # flat = Flat.objects.get(pk=flat_pk)
    room = Room.objects.get(pk=room_pk)
    cleans = CleanUp.objects.filter(room=room)
    return render(request, '../templates/admin/api/record/cleanup.html', {'cleans': cleans})


def load_points(request):
    clean_pk = request.GET.get('clean_pk')
    room_pk = request.GET.get('room_pk')
    room = Room.objects.get(pk=room_pk)
    clean = CleanUp.objects.filter(room=room).get(pk=clean_pk)
    return render(request, '../templates/admin/api/record/points.html', {'clean': clean})


def load_rooms(request):
    pk = request.GET.get('flat_pk')
    flat = Flat.objects.get(pk=pk)
    rooms = Room.objects.filter(flat=flat)
    return render(request, '../templates/admin/api/record/flat.html', {'rooms': rooms})


def load_flatmate(request):
    pk = request.GET.get('flat_pk')
    flat = Flat.objects.get(pk=pk)
    flatmates = Flatmate.objects.filter(flat=flat)
    return render(request, '../templates/admin/api/record/flatmate.html', {'flatmates': flatmates})
