# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import request
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from Scouts.account_profile.forms import UserCreateForm
from Scouts.account_profile.models import Profile
from Scouts.accounts.forms import AppUserCreationForm

# from django.shortcuts import render

# from Scouts.accounts.forms import UserCreateForm
# from Scouts.accounts.models import Profile
# from Scouts.payments.models import Payment

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    model = UserModel
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('details user')

    def get_success_url(self):
        return reverse_lazy(
            'details user',
            kwargs={
                'pk': self.request.user.pk,
            }
        )


class SignOutView(auth_views.LogoutView):
    model = UserModel
    next_page = reverse_lazy('index')

