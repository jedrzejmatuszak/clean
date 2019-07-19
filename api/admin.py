from django.contrib import admin
from .models import Room, Flat, CleanUp, Record, Flatmate
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


@admin.register(CleanUp)
class CleanUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'room', 'get_flat')
    fields = ('name', 'points', 'room')

    def get_flat(self, obj):
        return obj.room.flat
    get_flat.short_description = 'Flat'


@admin.register(Flatmate)
class FlatmateAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat')
    fields = ('user', 'flat')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('flat', 'flatmate', 'room', 'cleanup', 'date', 'to_date', 'realized', 'points')
    fields = ('flat', 'flatmate', 'room', 'cleanup', 'to_date', 'points', 'realized')


UserAdmin.list_display = ('id', 'username', 'email', 'first_name', 'last_name',
                          'is_staff', 'date_joined', 'last_login')
UserAdmin.ordering = ['id', ]
