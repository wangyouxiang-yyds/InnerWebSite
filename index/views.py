from django.shortcuts import render
from .models import *
# Create your views here.

# 首頁
def homepage(request):
    banner_first = HomeBanner1.objects.first()
    banner_second = HomeBanner2.objects.first()
    banner_third = HomeBanner3.objects.first()
    banner_fourth = HomeBanner4.objects.first()
    return render(request, 'index.html', locals())


