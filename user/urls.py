from django.urls import path,include
from .views import *

app_name='user'
urlpatterns = [
    path('login.html',loginView,name='login'),
    path('logout.html',logoutView,name='logout'),
    path('home/<int:page>.html',homeView,name='home')
]