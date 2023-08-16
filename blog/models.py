from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, **NULLABLE, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Превью')
    creation_date = models.DateField(verbose_name='Дата создания', **NULLABLE)
    publication_attribute = models.BooleanField(default=True, verbose_name='Опубликовать')
    number_of_views = models.IntegerField(default=0, verbose_name='Количество просмотров', **NULLABLE)

    def __str__(self):
        return f'{self.title} ({self.creation_date})'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
