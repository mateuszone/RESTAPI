from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# sender to zmiana w modelu User ktora aktywuje dekorator receiver ktory nasluchuje na zmiany w tym modelu post_save
# czy po dodaniu nowego uzytkownika do bazy

class Film(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    released = models.BooleanField(default=False)
    premiere = models.DateField(null=True, blank=True)
    year = models.IntegerField(default=2000)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    extra_info = models.OneToOneField("ExtraInfo", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.our_name()

    def our_name(self):
        return self.title + "( " + str(self.year) + " )"


class ExtraInfo(models.Model):
    CHOICES = {
        (0, 'Undefined'),
        (1, 'Horror'),
        (2, 'Sci=fi'),
        (3, 'Drama'),
        (4, 'Comedy'),
    }

    duration = models.IntegerField()
    genre = models.IntegerField(choices=CHOICES, default=0)


class Review(models.Model):
    description = models.TextField(default='')
    rating = models.IntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')


class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    films = models.ManyToManyField(Film, related_name='films')
