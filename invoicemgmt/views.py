from django.shortcuts import render, redirect
from .forms import InvoiceForm, InvoiceSearchForm
from .models import *
from invmgmt.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
	title = 'Home'
	total_invoices = Invoice.objects.count()
	total_stocks = Stock.objects.count()
	queryset1 = Stock.objects.order_by('-category')[:3]
	queryset = Invoice.objects.order_by('-invoice_date_created')[:3]
	context = {
	"title": title,
	"total_invoices": total_invoices,
	"total_stocks": total_stocks,
	"queryset": queryset,
	"queryset1": queryset1,

	}
	return render(request, "home.html",context)

@login_required
def create_invoice(request):
	form = InvoiceForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_invoice')
	context = {
		"form": form,
		"title": "New Invoice",
	}
	return render(request, "entry.html", context)

@login_required
def list_invoice(request):
	queryset = Invoice.objects.all()
	form = InvoiceSearchForm(request.POST or None)

	context = {
		"queryset": queryset,
		"form": form,
	}

	if request.method == 'POST':
		queryset = Invoice.objects.filter(name__icontains=form['name'].value())

		context = {
		"form": form,
		"queryset": queryset,
	}
	return render(request, "list_view.html", context)

@login_required
def delete_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_invoice')
	return render(request, 'delete_invoice.html')



