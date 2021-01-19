from django.urls import include, path

from . import  views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='index'),
    path('board-create', views.BoardCreateView.as_view(), name='board-create'),
    path('<str:number>',views.BoardDetailView.as_view(), name='board-detail'),
    path('card-change-lane/<int:board_id>/<str:action>/<int:card_id>', views.card_change_lane_view, name='card-change-lane'),
]
