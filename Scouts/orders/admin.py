from django.contrib import admin

from Scouts.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_to_deliver', 'quantity', 'category', 'item_name', 'ages', 'size', 'gender', 'place_to_deliver', 'comments', 'publication_date', 'user')
    list_filter = ('category', 'item_name', 'ages', 'size', 'gender', 'publication_date','place_to_deliver', )
    ordering = ('-publication_date', 'place_to_deliver', 'user', 'category', )
