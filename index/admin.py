from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title='我的音乐后台系统'
admin.site.site_header='我的音乐'#修改名称

admin.site.register(Label)
admin.site.register(Song)
admin.site.register(Dynamic)
admin.site.register(Comment)