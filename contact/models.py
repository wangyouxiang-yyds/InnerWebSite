from django.db import models

# 刪除資料連同圖片
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.

class ContactModels(models.Model):
    name = models.CharField(verbose_name="名字", max_length=20)
    department = models.CharField(verbose_name="部門", max_length=10)
    email = models.EmailField(verbose_name="電子信箱", max_length=200)
    message = models.TextField(verbose_name="訊息內容", blank=True)
    serial_number = models.CharField(verbose_name="工號", max_length=255)
    modify_date = models.DateTimeField(verbose_name='修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField(verbose_name='建立時間', auto_now_add=True)  # 新增時間
    is_reply = models.BooleanField(verbose_name="使否回覆", default=False)

    class Meta:
        db_table = 'contact'
        verbose_name_plural = '連絡我們'

    def __str__(self):
        return self.name


class ContactBanner(models.Model):
    banner_photo = models.ImageField(upload_to='BlogBannerPhoto', max_length=255,
                                     verbose_name="文章Banner圖")  # 文章banner圖
    modify_date = models.DateTimeField(verbose_name='修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField(verbose_name='建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'contact_banner'  # 資料表名稱
        verbose_name_plural = '文章Banner圖片'  # 後台選項名稱


# ------------------------------------------ 刪除照片 ------------------------------------------
@receiver(pre_delete, sender=ContactBanner)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)
