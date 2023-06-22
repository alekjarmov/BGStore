# Generated by Django 4.2 on 2023-04-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_language"),
    ]

    operations = [
        migrations.RemoveField(model_name="language", name="products",),
        migrations.AddField(
            model_name="product",
            name="languages",
            field=models.ManyToManyField(blank=True, to="store.language"),
        ),
    ]
