# Generated by Django 4.1.5 on 2023-01-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_product_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(blank=True, default='product_avatar/default.jpg', null=True, upload_to='product_avatar', verbose_name='Аватар'),
        ),
    ]
