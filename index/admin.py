from django.contrib import admin
from .models import *


# Register your models here.

class RunHorseLightAdmin(admin.ModelAdmin):
    list_display = ['display_or_not', 'announcement', 'modify_date', 'modify_user']
    admin_order = 1
admin.site.register(RunHorseLight, RunHorseLightAdmin)


class HomeBanner1Admin(admin.ModelAdmin):
    list_display = ['banner_photo', 'modify_date', 'create_date']
    admin_order = 2
admin.site.register(HomeBanner1, HomeBanner1Admin)


class HomeBanner2Admin(admin.ModelAdmin):
    list_display = ['banner_photo', 'modify_date', 'create_date']
    admin_order = 3

admin.site.register(HomeBanner2, HomeBanner2Admin)


class HomeBanner3Admin(admin.ModelAdmin):
    list_display = ['banner_photo', 'modify_date', 'create_date']

    admin_order = 4
admin.site.register(HomeBanner3, HomeBanner3Admin)


class HomeBanner4Admin(admin.ModelAdmin):
    list_display = ['banner_photo', 'modify_date', 'create_date']
    admin_order = 5

admin.site.register(HomeBanner4, HomeBanner4Admin)



