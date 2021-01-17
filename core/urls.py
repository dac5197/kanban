from django.urls import include, path

from . import  views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='index'),
    path('<str:number>',views.BoardDetailView.as_view(), name='board-detail')
]
