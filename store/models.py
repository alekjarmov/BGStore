from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(blank=False)  # actually is >= 0
    stock = models.PositiveIntegerField(default=0)
    image_url = models.URLField(max_length=7919)
    video_url = models.URLField(max_length=7919, blank=True, default="")
    copies_sold = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, default="")
    languages = models.ManyToManyField("Language", blank=True, related_name="products")
    # objects = ProductManager()

    def __str__(self):
        return self.name

    def get_short_description(self):
        return self.description.split("\n")[0]

    def save(self, *args, **kwargs):
        print("Saving product")
        super().save(*args, **kwargs)
        # check if we have 0 langugages
        if self.languages.count() == 0:
            # add english as default
            print("Adding english as default")
            self.languages.add(Language.objects.get(code="en"))


class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True, default="")
    image_url = models.URLField(max_length=7919)

    def __str__(self):
        return self.name
