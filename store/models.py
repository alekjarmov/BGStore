from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(blank=False)  # actually is >= 0
    stock = models.PositiveIntegerField(default=0)
    image_url = models.URLField(max_length=7919)
    video_url = models.URLField(max_length=7919, blank=True, default="")
    copies_sold = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name
