from django.conf.urls import url
from . import views			#导入全部视图

urlpatterns = [
	#只匹配空字符，即若访问127.0.0.1:8000则跳转到post_list这个视图
	#name 是url的名字，用来唯一标识一个视图
	url(r'^$', views.post_list, name='post_list')
]