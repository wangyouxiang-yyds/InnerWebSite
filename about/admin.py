from django.contrib import admin
from .models import *


# Register your models here.


class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ['banner_photo', 'modify_date', 'create_date']
    admin_order = 1


admin.site.register(AboutBanner, AboutBannerAdmin)


class AboutPhotoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'modify_date', 'create_date']
    admin_order = 2


admin.site.register(AboutPhoto, AboutPhotoAdmin)


class AboutIntroduceAdmin(admin.ModelAdmin):
    list_display = ['first_line', 'second_line', 'third_line', 'modify_date', 'create_date']
    admin_order = 3


admin.site.register(AboutIntroduce, AboutIntroduceAdmin)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'name', 'position']
    admin_order = 4


admin.site.register(Quote, QuoteAdmin)
