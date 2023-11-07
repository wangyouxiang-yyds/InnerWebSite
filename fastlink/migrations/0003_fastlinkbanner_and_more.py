# Generated by Django 4.2.4 on 2023-11-03 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fastlink", "0002_formlink_form_link_alter_formlink_create_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="FastLinkBanner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "banner_photo",
                    models.ImageField(max_length=255, upload_to="FastLinkBannerPhoto"),
                ),
                (
                    "modify_date",
                    models.DateTimeField(auto_now=True, verbose_name="修改時間"),
                ),
                (
                    "create_date",
                    models.DateField(auto_now_add=True, verbose_name="建立時間"),
                ),
            ],
            options={
                "verbose_name_plural": "表單連結Banner圖片",
                "db_table": "fast_link_banner",
            },
        ),
        migrations.AlterField(
            model_name="formlink",
            name="department_form_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="fastlink.departmentformcategory",
                verbose_name="部門",
            ),
        ),
    ]
