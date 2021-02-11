from django.urls import include, path

from . import  views

urlpatterns = [
    #Board views
    path('', views.BoardListView.as_view(), name='index'),
    path('board-create', views.BoardCreateView.as_view(), name='board-create'),
    path('<str:number>/', views.BoardDetailView.as_view(), name='board-detail'),
    #Lane views
    path('lane-list', views.LaneListView.as_view(), name='lane-list'),
    path('lane-create/<str:number>', views.LaneCreateView.as_view(), name='lane-create'),
    path('lane-update/<str:number>', views.LaneUpdateView.as_view(), name='lane-update'),
    path('lane-delete/<str:number>', views.LaneDeleteView.as_view(), name='lane-delete'),
    #Card views
    path('card-list', views.CardListView.as_view(), name='card-list'),
    path('card-update/<str:number>', views.CardUpdateView.as_view(), name='card-update'),
    path('card-delete/<str:number>', views.CardDeleteView.as_view(), name='card-delete'),
    #Function views
    path('card-change-lane/<int:board_id>/<str:action>/<int:card_id>', views.card_change_lane_view, name='card-change-lane'),
    path('create_defualt_lanes/<str:number>', views.create_defualt_lanes, name='create-defualt-lanes'),
]
