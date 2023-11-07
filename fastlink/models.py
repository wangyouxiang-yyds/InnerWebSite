from django.db import models


# Create your models here.


class DepartmentFormCategory(models.Model):
    department_name = models.CharField("部門", max_length=10)

    class Meta:
        db_table = 'department_form_category'
        verbose_name_plural = '部門'  # 後台選項名稱

    def __str__(self):
        return self.department_name


class FormLink(models.Model):
    department_form_category = models.ForeignKey(DepartmentFormCategory, on_delete=models.CASCADE, verbose_name='部門')
    form_name = models.CharField(verbose_name="表單名稱", max_length=50)
    form_link = models.CharField(verbose_name="表單連結", max_length=255)
    modify_date = models.DateField(verbose_name="修改日期", auto_now=True)
    modify_user = models.CharField(verbose_name="修改者", max_length=50, null=True)  # 修改者
    create_date = models.DateField(verbose_name="建立日期", auto_now=True)

    class Meta:
        db_table = 'formlink'
        verbose_name_plural = '表單'


class FastLinkBanner(models.Model):
    banner_photo = models.ImageField(upload_to='FastLinkBannerPhoto', max_length=255)  # 關於我們banner圖
    modify_date = models.DateTimeField(verbose_name='修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField(verbose_name='建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'fast_link_banner'  # 資料表名稱
        verbose_name_plural = '表單連結Banner圖片'  # 後台選項名稱


class common_link(models.Model):
    link_title = models.CharField(verbose_name="常用連結名稱", max_length=50, null=False)  # 表單名稱
    link_href = models.CharField(verbose_name="使用連結或說明", max_length=100, null=False)  # 表單名稱)
    modify_date = models.DateTimeField(verbose_name='修改時間', auto_now=True)  # 修改時間
    create_date = models.DateField(verbose_name='建立時間', auto_now_add=True)  # 新增時間

    class Meta:
        db_table = 'common_link'  # 資料表名稱
        verbose_name_plural = '常用連結'  # 後台選項名稱