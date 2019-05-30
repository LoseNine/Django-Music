from django.shortcuts import render,redirect
from user.models import *
from django.db.models import Q
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
from .forms import MyUserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from index.models import *

# Create your views here.
def loginView(req):
    user=MyUserCreationForm()
    if req.method=='POST':
        if req.POST.get('loginUser',''):
            loginUser=req.POST.get('loginUser','')
            password=req.POST.get('password','')
            if MyUser.objects.filter(Q(username=loginUser)|Q(mobile=loginUser)):
                user=MyUser.objects.filter(Q(username=loginUser)|Q(mobile=loginUser)).first()
                if check_password(password,user.password):
                    login(req,user)
                    return redirect('/user/home/1.html')
                else:
                    tips='密码错误'
        else:
            user=MyUserCreationForm(req.POST)
            if user.is_valid():
                user.save()
                tips='注册成功'
            else:
                if user.errors.get('username',''):
                    tips=user.errors.get('username','注册失败')
                else:
                    tips = user.errors.get('mobile', '注册失败')
    return render(req,'login.html',locals())

def logoutView(req):
    logoutView(req)
    return redirect('/')

@login_required(login_url='/user/login.html')
def homeView(req,page):
    #热搜歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    song_info=req.session.get('play_list','')
    paginator=Paginator(song_info,3)
    try:
        contacts=paginator.page(paginator)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(paginator.num_pages)
    return render(req,'home.html',locals())