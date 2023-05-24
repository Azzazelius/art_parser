from django.db import models
from urllib.parse import quote


class VkGroups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name


class VkImages(models.Model):
    album_id = models.IntegerField
    image_id = models.IntegerField
    group_id = models.ForeignKey(VkGroups, on_delete=models.CASCADE, null=True, blank=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    url = models.TextField()

# This function is used to escape 'url' values. It will work automatically, so I don't need to call it manually.
# escape = экранирование
    def save(self, *args, **kwargs):
        self.url = quote(self.url)
        super().save(*args, **kwargs)

    # class Meta: # couldn't find a way to use composite primary key =(
    #     unique_together = ('album_id', 'image_id')  # use this pair as a primary key

    def __str__(self):
        return f"Image {self.image_id} in Album {self.album_id}"

