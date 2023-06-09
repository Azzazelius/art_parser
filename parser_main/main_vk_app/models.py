from django.db import models
from urllib.parse import quote

'''
План капкан! 
Тут описываю структуру базы данных. 
А какими данными она будет заполняться будет настраиваю в pars_vk.py 
'''

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! удалить создание поля id, оно создаётся автоматически. Ручное создание помешает.


class Owners(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Albums(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owners, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class VkImages(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(null=True, blank=True)
    thumbnail = models.TextField()
    big_picture = models.TextField()

# This function is used to escape 'url' values. It will work automatically, so I don't need to call it manually.
# escape = экранирование
    def save(self, *args, **kwargs):
        self.url = quote(self.url)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image {self.id} in Album {self.album_id}"

