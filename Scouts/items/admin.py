from django.contrib import admin

from Scouts.items.models import Item, UsedItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'name', 'price', 'category', 'ages', 'size', 'gender', 'publication_date', 'location', 'user',)
    list_filter = ('category', 'ages', 'size', 'gender', 'location')
    ordering = ('category',)


@admin.register(UsedItem)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'category', 'ages', 'size', 'gender', 'publication_date', 'location', 'user')
    list_filter = ('category', 'ages', 'size', 'gender',)
    ordering = ('publication_date','category',)
