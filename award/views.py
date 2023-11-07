from django.shortcuts import render
from .models import *


# Create your views here.


def awardView(request):
    award_info = Award.objects.all().order_by('pk', 'create_date')
    banner = AwardBanner.objects.first()  # banner 圖片
    return render(request, 'award.html', locals())
