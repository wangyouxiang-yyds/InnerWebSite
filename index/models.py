'''
    啟用admin管理介面
    python manage.py createsuperuser
'''

from django.db import models
# 刪除資料連同圖片
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.
class HomeBanner1(models.Model):
    banner_photo = models.ImageField(upload_to='HomeBannerPhoto1', max_length=255)  # 首頁banner圖
    modify_date = models.DateTimeField('修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField('建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'home_banner_first'  # 資料表名稱
        verbose_name_plural = '首頁第一區塊圖片'  # 後台選項名稱


class HomeBanner2(models.Model):
    banner_photo = models.ImageField('圖片', upload_to='HomeBannerPhoto2', max_length=255)  # 首頁banner圖
    modify_date = models.DateTimeField('修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField('建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'home_banner_second'  # 資料表名稱
        verbose_name_plural = '首頁第二區塊圖片'  # 後台選項名稱


class HomeBanner3(models.Model):
    banner_photo = models.ImageField('圖片', upload_to='HomeBannerPhoto3', max_length=255)  # 首頁banner圖
    modify_date = models.DateTimeField('修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField('建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'home_banner_third'  # 資料表名稱
        verbose_name_plural = '首頁第三區塊圖片'  # 後台選項名稱


class HomeBanner4(models.Model):
    banner_photo = models.ImageField('圖片', upload_to='HomeBannerPhoto4', max_length=255)  # 首頁banner圖
    modify_date = models.DateTimeField('修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField('建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'home_banner_fourth'  # 資料表名稱
        verbose_name_plural = '首頁第四區塊圖片'  # 後台選項名稱


# 跑馬燈
class RunHorseLight(models.Model):
    display_or_not = models.BooleanField("是否要顯示")
    announcement = models.CharField("公告文字", max_length=100, null=False)  # 公告內容
    modify_date = models.DateTimeField("修改時間", auto_now=True)  # 修改時間
    modify_user = models.CharField("修改者", max_length=50, null=False)  # 修改者

    class Meta:
        db_table = 'marquee'  # 資料表名稱
        verbose_name_plural = '跑馬燈'  # 後台選項名稱

    def __str__(self):
        return self.announcement




# ------------------------------------------ 刪除照片 ------------------------------------------
@receiver(pre_delete, sender=HomeBanner1)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)


@receiver(pre_delete, sender=HomeBanner2)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)


@receiver(pre_delete, sender=HomeBanner3)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)

@receiver(pre_delete, sender=HomeBanner4)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)

