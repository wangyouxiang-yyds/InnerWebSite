# Generated by Django 4.2.4 on 2023-11-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactBanner",
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
                    models.ImageField(
                        max_length=255,
                        upload_to="BlogBannerPhoto",
                        verbose_name="文章Banner圖",
                    ),
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
                "verbose_name_plural": "文章Banner圖片",
                "db_table": "contact_banner",
            },
        ),
        migrations.CreateModel(
            name="ContactModels",
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
                ("name", models.CharField(max_length=20, verbose_name="名字")),
                ("department", models.CharField(max_length=10, verbose_name="部門")),
                ("email", models.EmailField(max_length=200, verbose_name="電子信箱")),
                ("message", models.TextField(blank=True, verbose_name="訊息內容")),
                ("serial_number", models.CharField(max_length=255, verbose_name="工號")),
                (
                    "modify_date",
                    models.DateTimeField(auto_now=True, verbose_name="修改時間"),
                ),
                (
                    "create_date",
                    models.DateField(auto_now_add=True, verbose_name="建立時間"),
                ),
                ("is_reply", models.BooleanField(default=False, verbose_name="使否回覆")),
            ],
            options={
                "verbose_name_plural": "連絡我們",
                "db_table": "contact",
            },
        ),
    ]