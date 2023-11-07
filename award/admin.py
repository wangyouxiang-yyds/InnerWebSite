from django.contrib import admin
# Register your models here.
from .models import *


class AwardBannerAdmin(admin.ModelAdmin):
    list_display = ['banner_photo', 'modify_date', 'create_date']
    admin_order = 1


admin.site.register(AwardBanner, AwardBannerAdmin)


class AwardAdmin(admin.ModelAdmin):
    list_display = ['big_title', 'award_photo', 'small_title', 'modify_date', 'create_date']
    admin_order = 2


admin.site.register(Award, AwardAdmin)
