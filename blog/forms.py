from django import forms
from .models import Post

#表单PostForm是一个ModelForm
class PostForm(forms.ModelForm):
	
	#model指明Post模型来创建表单
	#fields指明哪些字段会出现在表单中（author为当前user，create_date应当自动分配）
	class Meta:
		model = Post
		fields = ('title', 'text')