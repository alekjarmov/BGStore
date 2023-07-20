from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:product_id>", views.product, name="product"),
    path("products", views.products, name="products"),
    path("buy/<int:product_id>", views.buy, name="buy"),
    path("payment/<int:product_id>", views.payment, name="payment"),
    path("categories/<int:category_id>", views.categories, name="categories"),
]