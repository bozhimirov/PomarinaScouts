from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.core import validators
#
# from Scouts.accounts.models import Profile
# from Scouts.core.form_mixins import DisabledFormMixin
# from Scouts.core.validators import validate_only_letters, validate_only_numbers

UserModel = get_user_model()


class AppUserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email',)
        labels = {
            'email': 'Email',
        }


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2')
        # field_classes = {'username': UsernameField}
