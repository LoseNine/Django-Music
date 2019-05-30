from django.urls import path,include
from .views import *

app_name='comment'
urlpatterns = [
    path('<int:song_id>.html',commentView,name='comment')
]