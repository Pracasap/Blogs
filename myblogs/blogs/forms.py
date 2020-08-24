from django import forms
from .models import Blogs

class Form(forms.ModelForm):
	class Meta:
		model = Blogs
		fields = [
			'author',
			'title',
			'body'
			]