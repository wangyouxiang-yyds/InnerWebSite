from django.db import models
# 刪除資料連同圖片
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.

class BlogBanner(models.Model):
    banner_photo = models.ImageField(upload_to='BlogBannerPhoto', max_length=255,
                                     verbose_name="文章Banner圖")  # 文章banner圖
    modify_date = models.DateTimeField(verbose_name='修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField(verbose_name='建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'blog_banner'  # 資料表名稱
        verbose_name_plural = '文章Banner圖片'  # 後台選項名稱


class article_category(models.Model):  # 文章類別
    article_category = models.CharField('文章類別', max_length=10, null=False)

    class Meta:
        db_table = "article_category"
        verbose_name_plural = "文章類別"

    def __str__(self):
        return self.article_category


class article(models.Model):  # 文章
    title = models.CharField(verbose_name="標題", max_length=50, null=False)  # 標題
    small_title = models.CharField(verbose_name="小標題", max_length=100, null=False)  # 小標題
    content = models.TextField(verbose_name="文案", blank=True)  # 內文
    author_name = models.CharField(verbose_name="作者", max_length=10, null=False)  # 作者
    article_category = models.ForeignKey(article_category, on_delete=models.CASCADE,
                                         verbose_name="文章類別")  # foreign key
    modify_date = models.DateTimeField(auto_now=True, verbose_name="修改時間")  # 修改時間
    create_date = models.DateField(auto_now_add=True, verbose_name="新增時間")  # 新增時間
    article_photo = models.ImageField(verbose_name="文章圖片", upload_to='article_photo', max_length=255)

    class Meta:
        db_table = "article"
        verbose_name_plural = "文章內容"

    def __str__(self):
        return self.title


# ------------------------------------------ 刪除照片 ------------------------------------------
@receiver(pre_delete, sender=article)
def file_delete(sender, instance, **kwargs):
    instance.article_photo.delete(True)


@receiver(pre_delete, sender=BlogBanner)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)
