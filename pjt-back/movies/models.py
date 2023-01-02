from django.db import models
from django.conf import settings
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=128)
    score = models.FloatField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()
    exp_reple = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    def __str__(self):
        return self.title


class One_line_comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=150, null=True)
    grade = models.FloatField()
    like_comment_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like_comment_users")
    def __str__(self):
        return self.content


class RecommendMovie(models.Model):
    idx = models.IntegerField(primary_key=True)
    adult = models.BooleanField()
    backdrop_path = models.TextField()
    id = models.IntegerField()
    title = models.CharField(max_length=128)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=128)
    overview = models.TextField()
    poster_path = models.TextField()
    media_type = models.CharField(max_length=128)
    genre_ids = models.CharField(max_length=128)
    popularity = models.FloatField()
    release_date = models.DateField()
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()