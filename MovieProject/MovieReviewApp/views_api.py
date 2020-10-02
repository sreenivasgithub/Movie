from .serializers import movieinfoserializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MovieInfo


class movieList(APIView):
    def get(self, request):
        movie_info = MovieInfo.objects.all()
        serializer = movieinfoserializers(movie_info, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_single(request, pk):
    single_movie_info = MovieInfo.objects.get(id=pk)
    serializer = movieinfoserializers(single_movie_info, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMovie(request, pk):
    single_movie = MovieInfo.objects.get(id=pk)
    single_movie.delete()
    return Response('Deleted Successfully')