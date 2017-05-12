from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/homepage/$', views.homepage, name = 'homepage')
    #url(r'^Sciencepage$', views.science, name = 'science')
    #    url(r'^books/$', views.BookListView.as_view(), name='books'),    
]
