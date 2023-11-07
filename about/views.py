from django.shortcuts import render
from .models import *


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
    return render(request, 'about.html', locals())


