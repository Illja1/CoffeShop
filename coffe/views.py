from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def landing(request):
    return render (request, 'coffe/landing.html')
