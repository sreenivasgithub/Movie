from .serializers import movieinfoserializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from .models import MovieInfo

#@api_view(['GET',])
class movieList(APIView):
    def get(self, request):
        movie_info = MovieInfo.objects.all()
        serializer = movieinfoserializers(movie_info, many=True)
        return Response(serializer.data)