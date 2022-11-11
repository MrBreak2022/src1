from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

@login_required
def list_client(request):
	queryset2 = Client.objects.all()
	form = ClientCreateForm(request.POST or None)

	context = {
		"queryset2": queryset2,
		"form": form,
	}
	return render(request, "list_client.html", context)

@login_required
def add_client(request):
	form = ClientCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_client')
	context = {
		"form": form,
		"title": "Add Client",
	}
	return render (request, "add_client.html", context)

@login_required
def delete_client(request, pk):
	queryset2 = Client.objects.get(id=pk)
	if request.method == 'POST':
		queryset2.delete()
		return redirect('/list_client')
	return render(request, 'delete_client.html')