# Generated by Django 4.2.4 on 2023-11-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("award", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AwardBanner",
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
                        upload_to="AwardBannerPhoto",
                        verbose_name="獲得獎項Banner圖",
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
                "verbose_name_plural": "獲得獎項Banner圖片",
                "db_table": "award_banner",
            },
        ),
    ]
