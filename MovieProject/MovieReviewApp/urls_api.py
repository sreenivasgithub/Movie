from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from .import views_api
# from pdb import set_trace;set_trace()

urlpatterns = [
    url(r'^movieList/', views_api.movieList.as_view()),
    path('get_single/<str:pk>/', views_api.get_single, name='get_single'),
    path('deleteMovie/<str:pk>/', views_api.deleteMovie, name='deleteMovie'),
]