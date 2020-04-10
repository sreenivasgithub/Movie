from django import forms
from .models import MovieInfo

class MovieInfoForm(forms.ModelForm):
    class Meta:
        model = MovieInfo
        fields = ['movie_name', 'movie_type', 'movie_review', 'movie_date', 'movie_details']