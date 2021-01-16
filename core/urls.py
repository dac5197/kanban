from django.urls import include, path

from . import  views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='index'),
]
