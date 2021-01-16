from django.urls import include, path

from rest_framework.urlpatterns import format_suffix_patterns

from . import  views

urlpatterns = [
    path('boards/', views.BoardList.as_view()),
    path('boards/<int:pk>', views.BoardDetail.as_view()),

    path('lanes/', views.LaneList.as_view()),
    path('lanes/<int:pk>', views.LaneDetail.as_view()),

    path('cards/', views.CardList.as_view()),
    path('cards/<int:pk>', views.CardDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),

]