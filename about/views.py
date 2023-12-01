from django.shortcuts import render
from .models import *
from index.models import *
from django.urls import reverse
# Create your views here.


def aboutView(request):
    banner = AboutBanner.objects.first()     # banner 圖片
    photo = AboutPhoto.objects.first()       # 關於我們的圖片

    introduce_data = AboutIntroduce.objects.first()
    # 標題
    first_line = introduce_data.first_line
    # 第二標題
    second_line = introduce_data.second_line
    # 內文
    third_line = introduce_data.third_line

    quote = Quote.objects.all()
    display = RunHorseLight.objects.first() # 跑馬燈的抓取



    current_url = request.path_info
    about_url = reverse('about')
    return render(request, 'about.html', locals())


