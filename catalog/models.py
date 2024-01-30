from django.conf import settings
from django.db import models
from users.models import User


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='цена')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_of_last_changing = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Автор', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ('name',)

        permissions = [
                ('set_is_published', 'Can publish product'),
                ('set_category', 'Can change category'),
                ('set_description', 'Can change description'),
        ]    


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self) -> str:
        return f'{self.pk} {self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name', )


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=150, verbose_name='Название версии')
    number = models.FloatField(verbose_name='Номер версии')
    is_active = models.BooleanField(default=False, verbose_name='Активна')

    def __str__(self):
        return f'{self.name} {self.number}'
    
    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('is_active', 'name',)
        