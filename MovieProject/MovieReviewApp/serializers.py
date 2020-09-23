from rest_framework import serializers
from .models import MovieInfo

class movieinfoserializers(serializers.ModelSerializer):
    class Meta:
        model = MovieInfo
        #fields = ['movie_name', 'movie_type', 'movie_review', 'movie_date', 'movie_details']
        fields = '__all__'

