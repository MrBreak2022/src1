from django.shortcuts import render,redirect
from .models import *
from .forms import StockAddForm
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
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}

	return render(request, "list_view_item.html", context)

def delete_stock(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_stock')
	return render(request, 'delete_stock.html')

