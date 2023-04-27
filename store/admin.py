from django.contrib import admin

from .models import Product
from. models import Language

class ModelAdmin(admin.ModelAdmin):
    def save_related(self, request, form, formsets, change):
        super(ModelAdmin, self).save_related(request, form, formsets, change)
        language = Language.objects.get(code="en")
        if form.instance.languages.count() == 0:
            form.instance.languages.add(language)


# Register your models here.
admin.site.register(Product, ModelAdmin)
admin.site.register(Language, ModelAdmin)