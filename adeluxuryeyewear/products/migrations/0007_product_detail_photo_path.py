# Generated by Django 2.1.3 on 2018-12-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181201_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail_photo_path',
            field=models.CharField(default='/', max_length=25),
        ),
    ]
