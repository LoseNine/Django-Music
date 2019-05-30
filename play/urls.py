from django.urls import path,include
from .views import *

app_name='play'
urlpatterns = [
    path('<int:song_id>.html',playView,name='play'),
    path('download/<int:song_id>.html',downloadView,name='download')
]