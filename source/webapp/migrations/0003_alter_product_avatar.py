# Generated by Django 4.1.5 on 2023-01-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_product_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='product_avatar', verbose_name='Аватар'),
        ),
    ]
