from django.shortcuts import render,redirect
from .models import *
from .forms import StockAddForm, StockUpdateForm
# Create your views here.

def add_item(request):
	form = StockAddForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_stock')
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render (request, "add_item.html", context)

def list_stock(request):
	title = 'List of items:'
	queryset_stock = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset_stock,
	}

	return render(request, "list_view_item.html", context)

def delete_stock(request, pk):
	title = 'Confirm Delete'
	queryset = Stock.objects.get(id=pk)
	context = {
		"title": title,
	}
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_stock')
	return render(request, 'delete_stock.html')

def update_items(request, pk):
	title = 'Update'
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_stock')

	context = {
		'title': title,
		'form':form,
	}
	return render(request, 'add_item.html', context)
