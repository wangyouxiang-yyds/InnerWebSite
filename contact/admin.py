from django.contrib import admin
from .models import *


# Register your models here.


class ContactBannerAdmin(admin.ModelAdmin):
    ist_display = ['banner_photo', 'modify_date', 'create_date']
    admin_order = 1


admin.site.register(ContactBanner, ContactBannerAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['is_reply', 'name', 'department', 'email', 'message', 'serial_number', 'create_date']
    admin_order = 1


admin.site.register(ContactModels, ContactAdmin)
