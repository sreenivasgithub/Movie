from django.conf.urls import url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'admin', admin.site.urls),
    url(r'index', views.index, name='index'),
    url(r'addMovie', views.addMovie, name='addMovie'),
    url(r'result', views.result, name='result'),
    url(r'get_data', views.get_data, name='get_data'),
    url(r'single_movie', views.single_movie, name='single_movie'),
]