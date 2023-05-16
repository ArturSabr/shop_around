from django.contrib import admin
from.models import *
admin.site.register(Gallery)
admin.site.register(Pol)
admin.site.register(Category)
admin.site.register(Size)

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]