import django.utils.timezone as t
from django.db import models


class MovieInfo(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_type = models.CharField(max_length=200)
    movie_review = models.CharField(max_length=200)
    movie_date = models.CharField(max_length=200)
    movie_details = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.movie_name
    def __str__(self):
        return '%s --- %s' % (self.movie_name, self.movie_date)