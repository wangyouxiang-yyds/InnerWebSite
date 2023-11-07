from django.shortcuts import render
from .models import *
# Create your views here.


def contactView(request):




    return render(request, 'contact.html', locals())
