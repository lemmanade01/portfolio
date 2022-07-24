from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.urls import reverse
# from django.core.mail import send_mail
from .models import Contact
# import json

def homepage(request):
    """Show homepage."""

    return render(request, 'portfolio_app/homepage.html')

def about(request):
    return render(request, 'portfolio_app/about.html')

def work(request):
    return render(request, 'portfolio_app/work.html')

def contact(request):
    #TODO retrieve user data and create new Contact instance in database
    
    return render(request, 'portfolio_app/contact.html')