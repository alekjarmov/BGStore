from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField() # actually is >= 0
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


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="items")
    # objects = CartItemManager()

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"

    def get_total_price(self):
        return self.quantity * self.product.price


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"