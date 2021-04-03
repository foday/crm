from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here: home, products, customer.
def home(request):
    #return HttpResponse('home')
    return render(request, 'accounts/dashboard.html')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')
