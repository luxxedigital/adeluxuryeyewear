# Generated by Django 2.1.3 on 2018-12-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181201_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='special',
            field=models.CharField(choices=[('NS', 'Not Special'), ('WC', 'Wooden Collection')], default='NS', max_length=2),
        ),
    ]