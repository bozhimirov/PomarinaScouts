from django.urls import path, include

from Scouts.items.views import add_item, details_item, edit_item, delete_item, details_used_item, add_used_item, \
    edit_used_item, contact_seller, delete_used_item
from Scouts.orders.views import add_order

urlpatterns = (

    path('add/', add_item, name='add item'),
    path('<int:pk>/', include([
        path('', details_item, name='details item'),
        path('add/', add_order, name='add order'),
        path('edit/', edit_item, name='edit item'),
        path('delete/', delete_item, name='delete item'),

    ])),
    path('add_used/', add_used_item, name='add used item'),
    path('used/<int:pk>/', include([
        path('', details_used_item, name='details used item'),
        path('edit/', edit_used_item, name='edit used item'),
        path('delete/', delete_used_item, name='delete used item'),
        path('contact/', contact_seller, name='contact seller'),
    ])),
)




