from django.urls import path, include

from Scouts.orders.views import details_order, edit_order, delete_order

urlpatterns = (

    path('<int:pk>/', include([
        path('', details_order, name='details order'),
        path('edit/', edit_order, name='edit order'),
        path('delete/', delete_order, name='delete order'),
    ])),

)
