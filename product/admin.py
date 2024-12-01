from django.contrib import admin

from .models import Product1,DataModel
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'price', 'is_published', 'created_at')
    list_display_links = ('id','name') 
    list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('name', 'price')
    ordering = ('price',)
    #exclude=('price',)

admin.site.register(Product1,ProductAdmin)
admin.site.register(DataModel)