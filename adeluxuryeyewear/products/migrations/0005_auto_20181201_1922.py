# Generated by Django 2.1.3 on 2018-12-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='promotional_price',
            new_name='original_price',
        ),
        migrations.AddField(
            model_name='product',
            name='special',
            field=models.CharField(choices=[('WC', 'Wooden Collection')], default=None, max_length=2),
        ),
    ]
