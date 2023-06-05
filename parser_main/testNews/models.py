from django.db import models

# В вашем коде вы можете указать, с какой базой данных вы хотите работать.
# Для этого используйте атрибут using в методах доступа к данным
# (например, objects.using('second_db').all()).
# Если атрибут using не указан, будет использована база данных, указанная как "default".


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=255)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публицации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    # указываем базу данных для модели
    using = 'second_db'   # в модели вы можете указать, к какой базе данных они относятся, с помощью атрибута using
