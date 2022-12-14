"""Scouts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from Scouts import settings
from Scouts.core.exception_handler import custom_handler500, page_not_found_handler

urlpatterns = [
    path('', include('Scouts.web.urls')),
    path('scouts_admin/', admin.site.urls),
    path('auth/', include('Scouts.accounts.urls')),
    path('users/', include('Scouts.account_profile.urls')),
    path('kids/', include('Scouts.kids.urls')),
    path('marketplace/', include('Scouts.items.urls')),
    path('orders/', include('Scouts.orders.urls')),
    path('payments/', include('Scouts.payments.urls')),
# ]
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found_handler
handler500 = custom_handler500
