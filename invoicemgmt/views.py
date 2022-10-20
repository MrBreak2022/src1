from django.shortcuts import render, redirect
from .forms import InvoiceForm, InvoiceSearchForm
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
	title = 'Home'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

def create_invoice(request):
	form = InvoiceForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully saved!')
		return redirect('create_invoice')
	context = {
		"form": form,
		"title": "New Invoice",
	}
	return render(request, "entry.html", context)

def list_invoice(request):
	title = 'List of invoices:'
	queryset = Invoice.objects.all()
	form = InvoiceSearchForm(request.POST or None)

	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
	}

	if request.method == 'POST':
		queryset = Invoice.objects.filter(name__icontains=form['name'].value()
										  )

		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_view.html", context)

def delete_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_invoice')
	return render(request, 'delete_invoice.html')