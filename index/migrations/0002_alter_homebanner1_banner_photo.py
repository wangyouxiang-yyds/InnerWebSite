# Generated by Django 4.2.4 on 2023-10-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homebanner1",
            name="banner_photo",
            field=models.ImageField(
                max_length=255, upload_to="HomeBannerPhoto1", verbose_name="首頁圖片"
            ),
        ),
    ]