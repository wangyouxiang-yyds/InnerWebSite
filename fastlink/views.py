from django.shortcuts import render
from .models import *
from django.urls import reverse

# Create your views here.

def fastlinkView(request):
    banner = FastLinkBanner.objects.first()  # banner 圖片
    categories = DepartmentFormCategory.objects.all()
    department_forms_by_category = {}

    for category in categories:
        forms = FormLink.objects.filter(department_form_category=category)
        department_forms_by_category[category] = forms

    fast_url = common_link.objects.all().order_by('-pk')

    current_url = request.path_info
    fastlink_url = reverse('fastlink')
    return render(request, 'fastlink.html', locals())
