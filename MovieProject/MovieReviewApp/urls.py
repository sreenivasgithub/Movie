from django.conf.urls import url
from django.contrib import admin
from .import views
# from pdb import set_trace;set_trace()

urlpatterns = [
    url(r'admin', admin.site.urls),
    url(r'index', views.index, name='index'),
    url(r'addMovie', views.addMovie, name='addMovie'),
    url(r'result', views.result, name='result'),
    url(r'get_data', views.get_data, name='get_data'),
    url(r'single_movie/(?P<id>\d+)', views.single_movie, name='single_movie'),
    url(r'update/(?P<id>\d+)', views.update, name='update'),
    url(r'save_update', views.save_update, name='save_update'),
    url(r'delete/(?P<id>\d+)', views.delete, name='delete'),
    url(r'Additional', views.Additional, name='Additional'),
]