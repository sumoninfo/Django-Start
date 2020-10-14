from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'employee/index.html')


def profile(request):
    return render(request, 'employee/profile.html')
