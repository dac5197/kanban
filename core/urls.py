from django.urls import include, path

from . import  views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='index'),
    path('board-create', views.BoardCreateView.as_view(), name='board-create'),
    path('<str:number>/', views.BoardDetailView.as_view(), name='board-detail'),
    path('lane-create/<str:number>', views.LaneCreateView.as_view(), name='lane-create'),
    path('lane-update/<str:number>', views.LaneUpdateView.as_view(), name='lane-update'),
    #path('<str:number>/', views.board_detail_view, name='board-detail'),
    path('card-change-lane/<int:board_id>/<str:action>/<int:card_id>', views.card_change_lane_view, name='card-change-lane'),
    path('create_defualt_lanes/<str:number>', views.create_defualt_lanes, name='create-defualt-lanes'),
]
