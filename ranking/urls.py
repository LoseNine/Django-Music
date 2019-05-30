from django.urls import path,include
from . import views

app_name='ranking'
urlpatterns = [
    path('',views.rankingView,name='ranking'),
    path('.list',views.RankingList.as_view(),name='rankingList')
]