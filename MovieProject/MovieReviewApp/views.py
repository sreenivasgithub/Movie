from django.shortcuts import render, HttpResponse, get_object_or_404
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
        return render(request, 'get_data.html')
    else:
        return HttpResponse('Error')
def get_data(request):
    fetch = MovieInfo.objects.all()
    return render(request, 'get_data.html', {'fetch':fetch})

def single_movie(request):
    # from pdb import set_trace;
    # set_trace()
    id = (request.GET.get('id'))
    movie = MovieInfo.objects.get(id=id)
    #movie = get_object_or_404(MovieInfo, id=id)
    return render(request, 'update.html', {'movie': movie})
# from pdb import set_trace;set_trace()

def update_movie(request):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", request)
    from pdb import set_trace;
    set_trace()
    if request.method == 'POST':
        id = request.GET.get('id')
        #item = get_object_or_404(MovieInfo, id=id)
        item = MovieInfo.objects.filter(pk=3)
        item.movie_name = request.POST['name']
        item.movie_type = request.POST['type']
        item.movie_review = request.POST['review']
        item.movie_date = request.POST['date']
        item.movie_details = request.POST['details']
        item.save()
        return HttpResponse('Updated')
    else:
        return HttpResponse('ErrorUpdate')
