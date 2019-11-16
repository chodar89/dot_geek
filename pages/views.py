from django.shortcuts import render

from .models import IndexCarousel

carousels = IndexCarousel.objects.all()

context = {
    'carousels': carousels
}

def index(request):
    return render(request, 'pages/index.html', context)
