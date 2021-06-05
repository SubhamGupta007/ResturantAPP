from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        'variable': "this is sent",
        'name': "this is my name"
    }
    # messages.success(request, 'test')
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return HttpResponse("this is services page")


def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(firstname='firstname', lastname=lastname,
                          email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')

    return render(request, 'contact.html')


def icecream(request):
    return render(request, 'icecream.html')


def softy(request):
    return render(request, 'softy.html')


def family(request):
    return render(request, 'family.html')
