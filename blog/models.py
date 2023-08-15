from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Entry(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Превью')
    creation_date = models.DateField(verbose_name='Дата создания')
    publication_attribute = models.BooleanField(default=True, verbose_name='Признак публикации')
    number_of_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} ({self.creation_date})'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'