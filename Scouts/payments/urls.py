from django.urls import path, include

from Scouts.payments.views import add_payment, details_payment, edit_payment, delete_payment, confirm_payment, \
    confirm_payment_by_staff

urlpatterns = (

    path('add/', add_payment, name='add payment'),  #add payment button from staff member in nav bar?
    path('<int:pk>/', include([
        path('', details_payment, name='details payment'),
        path('edit/', edit_payment, name='edit payment'),
        path('confirm/', confirm_payment, name='confirm payment'),
        path('paid/', confirm_payment_by_staff, name='confirm paid'),
        path('delete/', delete_payment, name='delete payment'),

    ])),
)
