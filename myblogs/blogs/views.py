from django.shortcuts import render
from .models import Blogs
from .forms import Form

# Create your views here.

def create_view(request):
	form = Form(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, 'blogcreate.html', context)


def detail_view(request):
	queryset = Blogs.objects.all()
	context = {
		'obj': queryset
	}
	return render(request, 'blogdisplay.html', context)
