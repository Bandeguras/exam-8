from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
CATEGORY_CHOICES = [('electronics', 'Электроника'), ('clothes', 'Одежда'), ('food', 'Еда')]
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="Заголовок")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name="Категория")
    description = models.TextField(max_length=3000, verbose_name="Описание", null=True, blank=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='product_avatar', verbose_name="Аватар")


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews', verbose_name='Продукт')
    description = models.TextField(max_length=3000, verbose_name="Описание")
    rating = models.PositiveIntegerField(verbose_name='Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])
    moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
