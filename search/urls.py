from django.urls import path,include
from .views import *

app_name='search'
urlpatterns = [
    path('<int:page>.html',searchView,name='search'),
]