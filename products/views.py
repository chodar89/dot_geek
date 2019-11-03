from django.shortcuts import render

# Create your views here.
def all_products(request):
    return render(request, 'products/products.html')

def product(request):
    return render(request, 'products/products.html')

def search(request):
    return render(request, 'products/products.html')
