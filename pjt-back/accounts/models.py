from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    score = models.IntegerField(default=0)
    visited = models.ManyToManyField(Movie, related_name="visited_movie", through='Time')

class Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    visit = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)