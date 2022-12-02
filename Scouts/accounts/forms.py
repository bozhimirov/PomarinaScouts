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
    PASSWORD_LENGTH = 20
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': "Email"}),
        error_messages={
            "unique": "A user with that email doesn't exists.",
        },
    )

    password1 = forms.CharField(
        max_length=PASSWORD_LENGTH,
        label="Password",
        widget=forms.PasswordInput(
            attrs={'placeholder': "Enter password here"}),
    )

    class Meta:
        model = UserModel
        fields = ('email',)
        labels = {
            'email': 'Email',
        }


class AppUserCreationForm(UserCreationForm):
    PASSWORD_LENGTH = 20
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': "Email"}),
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )

    password1 = forms.CharField(
        max_length=PASSWORD_LENGTH,
        label="Password",
        widget=forms.PasswordInput(
            attrs={'placeholder': "Enter password here"}),
    )

    password2 = forms.CharField(
        max_length=PASSWORD_LENGTH,
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={'placeholder': "Enter again the same password here"}),
    )

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2')
