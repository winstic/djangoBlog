from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
	#render方法渲染模板
	#获取Post查询集,注意published_date__lte中lte前的分隔符需要两个下划线__
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	#将posts数据集传递到模板文件中
	return render(request, 'blog/post_list.html', {'posts':posts})
	
def post_detail(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	return render(request, 'blog/post_detail.html', {'post':post})
	
def post_new(request):
	if request.method == 'POST':
		#如果method是POST就用表单里的数据构建PostForm
		form = PostForm(request.POST)
		if form.is_valid():
			#第一个save表示还不想保存表单，还要添加其他信息
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			#post.save()会保留更改，并创建新的博客文章
			post.save()
			#创建完后转到post_detail页面，当然需要传帖子id
			return redirect('post_detail', post_id=post.pk)
	else:
		#否则默认方法构建
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	if request.method == 'POST':
		#用实例instance来保存表单
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', post_id=post.pk)
	else:
		form = PostForm(instance = post)
	return render(request, 'blog/post_edit.html', {'form': form})