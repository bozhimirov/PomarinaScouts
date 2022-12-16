from django.urls import path, include

from Scouts.kids.views import add_kid, details_kid, edit_kid, delete_kid

urlpatterns = (
        path('add/', add_kid, name='add kid'),
        path('<str:uid>/kid/<slug:kid_slug>/', include([
            path('', details_kid, name='details kid'),
            path('edit/', edit_kid, name='edit kid'),
            path('delete/', delete_kid, name='delete kid'),
        ])
             ),
)

from .signals import *