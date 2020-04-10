from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import MovieInfo
from .forms import MovieInfoForm
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

def single_movie(request, id):
    #from pdb import set_trace;set_trace()
    #id = (request.GET.get('id'))
    movie = MovieInfo.objects.get(id=id)
    #movie = get_object_or_404(MovieInfo, id=id)
    return render(request, 'single_movie.html', {'movie': movie})

def update(request, id=None):
    #movie = get_object_or_404(MovieInfo, id=id)
    movie = MovieInfo.objects.get(id=id)
    return render(request, 'update.html', {'movie': movie})
def save_update(request):
    if request.method == "POST":
        #from pdb import set_trace;set_trace()
        obj = MovieInfo.objects.filter(movie_name=request.POST['name'])
        movie_name = request.POST["name"]
        movie_type = request.POST["type"]
        movie_review = request.POST["review"]
        movie_date = request.POST["date"]
        movie_details = request.POST["details"]
        obj.update(movie_name=movie_name, movie_type=movie_type, movie_review=movie_review,
                          movie_date=movie_date, movie_details=movie_details)
        return redirect('get_data')
    # else:
    #     return 'ERROR'
    # emp = MovieInfo.objects.get(pk=id)
    # emp.movie_name = request.POST.get('name')
    # emp.save()
    # return HttpResponse('updated')
def delete(request, id):
    #from pdb import set_trace;set_trace()
    a =MovieInfo.objects.get(pk=int(id))
    a.delete()
    return render(request,'index.html')
def Additional(request):
    return render(request, 'Additional.html')