from django.db.models import Q
from django.shortcuts import render
from .models import *
from django.urls import reverse
from blog.views import article
# Create your views here.

# 首頁
def homepage(request):
    banner_first = HomeBanner1.objects.first()
    banner_second = HomeBanner2.objects.first()
    banner_third = HomeBanner3.objects.first()
    banner_fourth = HomeBanner4.objects.first()
    display = RunHorseLight.objects.first()

    all_article_three = article.objects.all().order_by('-pk', 'create_date')[:3]    # 找最新三筆文章



    current_url = request.path_info
    index_url = reverse('index')
    return render(request, 'index.html', locals())



def baseView(request):
    all_article = article.objects.all().order_by('-pk', 'create_date')

    if 'search' in request.GET:
        search = request.GET['search']
        if len(search) > 0:
            all_article = article.objects.filter(Q(title__icontains=search) | Q(content__icontains=search)).order_by('-pk', 'create_date')

    return render(request, 'base.html', locals())


