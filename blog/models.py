from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Page(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержание')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликован')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name='Страница'
        verbose_name_plural = 'Страницы'