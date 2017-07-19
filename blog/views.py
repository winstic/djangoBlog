from django.shortcuts import render

# Create your views here.

def post_list(request):
	#render方法渲染模板
	return render(request, 'blog/post_list.html', {})