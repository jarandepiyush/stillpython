from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.

def index(request):
    # return HttpResponse("hi pj")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def product(request):
    return render(request, "product.html")

def pro1(request):
    return render(request, "pro1.html")

def pro2(request):
    return render(request, "pro2.html")

def pro3(request):
    return render(request, "pro3.html")

def pro4(request):
    return render(request, "pro4.html")

def pro5(request):
    return render(request, "pro5.html")

def pro6(request):
    return render(request, "pro6.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, "contact.html")
