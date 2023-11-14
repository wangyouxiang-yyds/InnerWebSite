from django.shortcuts import render
from .models import *
from django.urls import reverse

# Create your views here.


def awardView(request):
    award_info = Award.objects.all().order_by('pk', 'create_date')
    banner = AwardBanner.objects.first()  # banner 圖片

    current_url = request.path_info
    award_url = reverse('award')

    return render(request, 'award.html', locals())
