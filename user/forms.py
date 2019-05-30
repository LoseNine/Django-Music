from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#定义注册
class MyUserCreationForm(UserCreationForm):
    
    #重写初始化,设置密码字段
    def __init__(self,*args,**kwargs):
        super(MyUserCreationForm, self).__init__(*args,**kwargs)
        self.fields['password1'].widget=forms.PasswordInput(
            attrs={'class':'txt tabInput','placeholder':'密码，4-16位数字/字母/特殊符号'}
        )
        self.fields['password2'].widget=forms.PasswordInput(
            attrs={'class':'txt tabInput','placeholder':'重复密码'}
        )

    class Meta(UserCreationForm.Meta):
        model=MyUser
        fields=UserCreationForm.Meta.fields+('mobile',)
        
        #设置样式属性
        widgets={
            'username':forms.TextInput(attrs={'class':'txt tabInput','placeholder':'用户名'}),
            'mobile':forms.TextInput(attrs={'class':'txt tabInput','placeholder':'手机号'})
        }
        