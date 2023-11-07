from django.contrib import admin
from .models import *


# Register your models here.

class FastLinkBannerAdmin(admin.ModelAdmin):
    list_display = ['banner_photo', 'modify_date', 'create_date']
    admin_order = 1


admin.site.register(FastLinkBanner, FastLinkBannerAdmin)


class DepartmentFormCategoryAdmin(admin.ModelAdmin):
    list_display = ['department_name']
    admin_order = 2


admin.site.register(DepartmentFormCategory, DepartmentFormCategoryAdmin)


class FormLinkAdmin(admin.ModelAdmin):
    list_display = ['department_form_category', 'form_name', 'modify_user', 'modify_date', 'create_date']
    admin_order = 3


admin.site.register(FormLink, FormLinkAdmin)


class CommonLinkAdmin(admin.ModelAdmin):
    list_display = ['link_title', 'link_href', 'modify_date', 'create_date']
    admin_order = 4


admin.site.register(common_link, CommonLinkAdmin)
