from django.contrib import admin

from Scouts.items.models import Item, UsedItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('photo', 'name', 'price', 'category', 'ages', 'size', 'gender', 'publication_date', 'location', 'user',)
    list_filter = ('category', 'ages', 'size', 'gender', 'location', 'user')


@admin.register(UsedItem)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('photo', 'category', 'ages', 'size', 'gender', 'publication_date', 'location', 'user')
    list_filter = ('category', 'ages', 'size', 'gender',)
