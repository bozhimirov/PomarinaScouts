from django.urls import path

from Scouts.accounts.views import SignInView, SignOutView

urlpatterns = (

    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),

)



