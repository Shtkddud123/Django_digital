from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index')
    #url(r'^Sciencepage$', views.science, name = 'science')
    #    url(r'^books/$', views.BookListView.as_view(), name='books'),    
]
