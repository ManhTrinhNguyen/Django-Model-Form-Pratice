from django.shortcuts import render
from .forms import CustomerForm, OrderForm

# Create your views here.

def view_customer_form(request):
  # Create var for a form object 
  form = CustomerForm()
  if request.method == 'POST':
    # If method == post make form content into post method
    form = CustomerForm(request.POST)
    if form.is_valid():
      form.save()
  
  context = {'form': form}
  return render(request, 'add_customer.html', context)


def view_order_form(request):
  form = OrderForm()
  if request.method == 'POST':
    form = OrderForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form': form}
  return render(request, 'place_order.html', context)