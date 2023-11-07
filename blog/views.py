from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def blogView(request):
    all_article = article.objects.all().order_by('-pk', 'create_date')
    banner = BlogBanner.objects.first()  # banner 圖片
    all_article_three = article.objects.all().order_by('-pk', 'create_date')[:3]

    limit = 4
    page = request.GET.get('page', 1)
    paginator = Paginator(all_article, limit)
    try:
        all_article = paginator.page(page)
    except PageNotAnInteger:
        all_article = paginator.page(1)
    except EmptyPage:
        all_article = paginator.page(paginator.num_pages)
    return render(request, 'blog-sidebar.html', locals())


def blog_single_view(request, article_id):
    all_article = article.objects.all().order_by('-pk', 'create_date')  # -pk為降序 這邊說明為依照建立時間去排序
    previous_article = article.objects.filter(pk__lt=article_id).order_by('-pk').first()
    next_article = article.objects.filter(pk__gt=article_id).order_by('pk').first()
    article_obj = get_object_or_404(all_article, pk=article_id)
    current_url = request.path_info
    article_news_three = article.objects.all().order_by('-pk', 'create_date')[:3]  # -pk為降序 這邊說明為依照建立時間去排序 限制三筆
    banner = BlogBanner.objects.first()  # banner 圖片


    return render(request, 'blog-single.html', locals())