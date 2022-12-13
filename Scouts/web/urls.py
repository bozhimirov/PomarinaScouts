from django.urls import path

from Scouts.web.views import IndexView, SuccessView, ForParentsView, ContactsView, \
    scout_store, scout_store_new, scout_store_used, orders_all

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('success/', SuccessView.as_view(), name='success'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('for_parents/', ForParentsView.as_view(), name='for parents'),
    path('all/', orders_all, name='orders all'),
    path('scout_store/', scout_store, name='scout store'),
    path('scout_store_new/', scout_store_new, name='scout store new'),
    path('scout_store_used/', scout_store_used, name='scout store used'),
]
