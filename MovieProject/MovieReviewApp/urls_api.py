from django.conf.urls import url
from django.contrib import admin
from .import views_api
# from pdb import set_trace;set_trace()

urlpatterns = [
    url(r'^api/', views_api.movieList.as_view())
]