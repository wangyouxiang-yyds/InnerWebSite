from django.db import models

# Create your models here.


# 刪除資料連同圖片
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class AboutBanner(models.Model):
    banner_photo = models.ImageField(upload_to='AboutBannerPhoto', max_length=255)  # 關於我們banner圖
    modify_date = models.DateTimeField('修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField('建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'about_banner'  # 資料表名稱
        verbose_name_plural = '關於我們Banner圖片'  # 後台選項名稱


class AboutPhoto(models.Model):
    photo = models.ImageField(upload_to='about', max_length=255)    # 關於我們介紹圖片
    modify_date = models.DateTimeField('修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField('建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'about'  # 資料表名稱
        verbose_name_plural = '關於我們圖片'  # 後台選項名稱


class AboutIntroduce(models.Model):
    first_line = models.CharField('第一段字', max_length=10)
    second_line = models.CharField('第二段字', max_length=20)
    third_line = models.CharField('第三段字', max_length=255)
    modify_date = models.DateTimeField('修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField('建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'about_introduce'  # 資料表名稱
        verbose_name_plural = '關於介紹文字'  # 後台選項名稱


class Quote(models.Model):
    text = models.CharField('精神喊話', max_length=255)
    name = models.CharField('名字', max_length=20)
    position = models.CharField('職稱', max_length=10)

    class Meta:
        db_table = 'quote'
        verbose_name_plural = '主管的精神喊話'


# ------------------------------------------ 刪除照片 ------------------------------------------

@receiver(pre_delete, sender=AboutBanner)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)

@receiver(pre_delete, sender=AboutPhoto)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)


