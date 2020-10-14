from django.http import HttpResponse
from django.shortcuts import render

from index.models import About, Slider


def index(request):
    about_data = About.objects.all()[0]
    slider_data = Slider.objects.all()
    context = {
        'about': about_data,
        'sliders': slider_data
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

