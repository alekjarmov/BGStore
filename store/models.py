from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()  # actually is >= 0
    stock = models.IntegerField()
    image_url = models.URLField(max_length=7919)
    video_url = models.URLField(max_length=7919, blank=True, default="")

    def __str__(self):
        return self.name