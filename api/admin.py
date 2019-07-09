from django.contrib import admin
from .models import Room, Flat, Clean, Record, Flatmate
from django.contrib.auth.admin import UserAdmin


# Register your models here.


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'flat')
    fields = ('name', 'flat')


@admin.register(Clean)
class CleanAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'room')
    fields = ('name', 'points', 'room')


@admin.register(Flatmate)
class FlatmateAdmin(admin.ModelAdmin):
    list_display = ('username', 'flat')
    fields = ('username', 'flat')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('flat', 'room', 'clean', 'flatmate', 'date', 'to_date', 'realized', 'points')
    fields = ('flat', 'room', 'clean', 'flatmate', 'to_date', 'points')
    readonly_fields = ('points', )


UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name',
                          'is_staff', 'date_joined', 'last_login')
