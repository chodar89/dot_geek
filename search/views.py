from django.shortcuts import render

# Create your views here.

def search(request):
    """ Render search page with resualts"""
    
    return render(request, 'search/search.html')
