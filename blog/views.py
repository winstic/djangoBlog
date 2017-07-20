from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
	#render方法渲染模板
	#获取Post查询集,注意published_date__lte中lte前的分隔符需要两个下划线__
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	#将posts数据集传递到模板文件中
	return render(request, 'blog/post_list.html', {'posts':posts})