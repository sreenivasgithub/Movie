from django.shortcuts import render, HttpResponse
from .models import MovieInfo
# Create your views here.
def index(request):
    return render(request, 'index.html')
def addMovie(request):
    return render(request, 'addMovie.html')
def result(request):
    if request.method == 'POST':
        movie_name = request.POST["name"]
        movie_type = request.POST["type"]
        movie_review = request.POST["review"]
        movie_date = request.POST["date"]
        movie_details = request.POST["details"]

        movie = MovieInfo(movie_name=movie_name, movie_type=movie_type, movie_review=movie_review, movie_date=movie_date, movie_details=movie_details)
        movie.save()
        return render(request, 'index.html')
    else:
        return HttpResponse('Error')
def get_data(request):
    fetch = MovieInfo.objects.all()
    return render(request, 'get_data.html', {'fetch':fetch})
def single_movie(request):
    id = request.GET.get('id')
    movie = MovieInfo.objects.get(id=id)
    return render(request, 'single_movie.html', {'movie': movie})