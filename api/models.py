from django.db import models
from api_user.models import CustomUser

# Create your models here.


class Flat(models.Model):
    name = models.TextField()
    parent_mode = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.TextField()
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return f'{self.name} - {self.flat.name}'


class CleanUp(models.Model):
    name = models.TextField()
    points = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cleanup')

    def __str__(self):
        return self.name


class Flatmate(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='flatmates')

    def __str__(self):
        if self.user.first_name != '':
            return str(self.user.get_full_name())
        else:
            return self.user.username


class Record(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='flat_records')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_records')
    cleanup = models.ForeignKey(CleanUp, on_delete=models.CASCADE, related_name='cleanup_records')
    flatmate = models.ForeignKey(Flatmate, on_delete=models.CASCADE, related_name='flatmate_records')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateField()
    realized = models.BooleanField(default=False)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.room} - {self.cleanup} - {self.flatmate} - {self.to_date}"

    def save(self, *args, **kwargs):
        self.points = self.cleanup.points
        super(Record, self).save(*args, **kwargs)
