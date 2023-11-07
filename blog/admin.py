from django.contrib import admin
from .models import *


# Register your models here.

class ArticleBannerAdmin(admin.ModelAdmin):
    list_display = ['banner_photo', 'modify_date', 'create_date']
    admin_order = 1


admin.site.register(BlogBanner, ArticleBannerAdmin)


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['article_category']
    admin_order = 2


admin.site.register(article_category, ArticleCategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_category', 'title', 'small_title', 'author_name', 'modify_date', 'create_date']
    admin_order = 3


admin.site.register(article, ArticleAdmin)
