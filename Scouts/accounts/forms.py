from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.views.generic.edit import FormMixin

UserModel = get_user_model()


class AppUserEditForm(FormMixin, UserChangeForm):
    PASSWORD_LENGTH = 20

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Email"
            }
        ),

        error_messages={
            "unique": "A user with that email doesn't exists.",
        },
    )

    password1 = forms.CharField(
        max_length=PASSWORD_LENGTH,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Enter password here"
            }
        ),
    )

    class Meta:
        model = UserModel
        fields = ('email',)
        labels = {
            'email': 'Email',
        }
        field_classes = {
            "username": UsernameField,
        }


class AppUserCreationForm(FormMixin, UserCreationForm):
    PASSWORD_LENGTH = 20

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Email"
            }
        ),
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )

    password1 = forms.CharField(
        max_length=PASSWORD_LENGTH,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Enter password here"
            }
        ),
    )

    password2 = forms.CharField(
        max_length=PASSWORD_LENGTH,
        label="Password Confirmation",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Enter again the same password here"
            }
        ),
    )

    class Meta:
        model = UserModel
        fields = (
            UserModel.USERNAME_FIELD,
            'password1',
            'password2',
        )
