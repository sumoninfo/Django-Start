from django.http import HttpResponse
from django.shortcuts import render

from contact.models import Contact


def contact(request):
    if request.method == 'POST':
        contact_data = Contact()
        contact_data.name = request.POST.get('name')
        contact_data.email = request.POST.get('email')
        contact_data.subject = request.POST.get('subject')
        contact_data.message = request.POST.get('message')
        contact_data.save()

    return render(request, 'contact.html')
