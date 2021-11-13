from django.db import models


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.pk}: {self.name}'


class Movie(models.Model):
    adult = models.BooleanField()
    genre_ids  = models.ManyToManyField(Genre, related_name='movies')
    id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=50)
    original_title = models.CharField(max_length=255)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    release_date = models.DateTimeField()
    title = models.CharField(max_length=255)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    
    def __str__(self):
        return f'{self.pk}: {self.title}'
