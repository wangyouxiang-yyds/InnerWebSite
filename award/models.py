from django.db import models

# 刪除資料連同圖片
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.
class Award(models.Model):
    award_photo = models.ImageField(upload_to="award_photo", max_length=255, verbose_name="獎項圖片")
    big_title = models.CharField(verbose_name="大標題", max_length=50, null=True)
    small_title = models.CharField(verbose_name="小標題", max_length=50, null=True)
    modify_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")
    create_date = models.DateField(auto_now=True, verbose_name="建立日期")

    class Meta:
        db_table = "award"
        verbose_name_plural = "獲得獎項列表"

    def __str__(self):
        return self.big_title


class AwardBanner(models.Model):
    banner_photo = models.ImageField(upload_to='AwardBannerPhoto', max_length=255,
                                     verbose_name="獲得獎項Banner圖")  # 關於我們banner圖
    modify_date = models.DateTimeField(verbose_name='修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField(verbose_name='建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'award_banner'  # 資料表名稱
        verbose_name_plural = '獲得獎項Banner圖片'  # 後台選項名稱


# ------------------------------------------ 刪除照片 ------------------------------------------
@receiver(pre_delete, sender=AwardBanner)
def file_delete(sender, instance, **kwargs):
    instance.banner_photo.delete(True)


@receiver(pre_delete, sender=Award)
def file_delete(sender, instance, **kwargs):
    instance.award_photo.delete(True)
