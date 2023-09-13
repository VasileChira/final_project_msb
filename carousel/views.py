from django.shortcuts import render
from .models import Carousel

# Create your views here.
def HomeView(request):
    carousel = Carousel.objects.all()
    context  = {
        'carousel' : carousel
    }
    return render(request, 'homepage.html', context)