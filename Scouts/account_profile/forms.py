from django import forms
from django.contrib.auth import get_user_model
from django.core import validators

from Scouts.account_profile.models import Profile
from Scouts.accounts.forms import AppUserEditForm, AppUserCreationForm
from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.core.validators import validate_only_letters, validate_only_numbers, validate_mobile_number

UserModel = get_user_model()


class UserEditForm(DisabledFormMixin, AppUserEditForm):

    # disabled_fields = ('first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        MIN_LEN_FIRST_NAME = 2
        MAX_LEN_FIRST_NAME = 30
        MIN_LEN_LAST_NAME = 2
        MAX_LEN_LAST_NAME = 30
        MAX_LEN_PHONE = 10

        model = Profile
        fields = '__all__'

        first_name = forms.CharField(
            max_length=MAX_LEN_FIRST_NAME,
            label="First Name",
            widget=forms.TextInput(
                attrs={
                    'placeholder': "First Name:"
                }
            ),
            validators=(
                validators.MinLengthValidator(
                    MIN_LEN_FIRST_NAME
                ),
                validate_only_letters,
            ),
        )

        last_name = forms.CharField(
            max_length=MAX_LEN_LAST_NAME,
            label="Last Name",
            widget=forms.TextInput(
                attrs={
                    'placeholder': "Last Name:"
                }
            ),
            help_text="Please use only letters.",
            validators=(
                validators.MinLengthValidator(
                    MIN_LEN_LAST_NAME
                ),
                validate_only_letters,
            ),
        )

        phone_number = forms.CharField(
            max_length=MAX_LEN_PHONE,
            label="Phone Number",
            widget=forms.TextInput(
                attrs={
                    'placeholder': "Phone Number:"
                }
            ),
            validators=(
                validate_mobile_number,
                validate_only_numbers,
            ),
            error_messages={
                'required': 'Place phone number in format: 0987654321'
            },
            help_text="Type phone number in format: 0987654321",
        )
        CHOICES = [
            (None, 'Optional / Please choose gender'),
            ('Male', 'Male'),
            ('Female', 'Female')]
        gender = forms.ChoiceField(
            choices=CHOICES,
        )

        profile_image = forms.ImageField(
            required=False,
            label="Optional / Profile Image",
            widget=forms.TextInput(
                attrs={
                    'placeholder': " Optional / Profile Image:"
                }
            ),
            help_text="Upload your photo here",

        )


class UserCreateForm(AppUserCreationForm):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_PHONE = 10

    first_name = forms.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': "First name"
            }
        ),
        validators=(
            validators.MinLengthValidator(
                MIN_LEN_FIRST_NAME
            ),
            validate_only_letters,
        ),
    )

    last_name = forms.CharField(
        max_length=MAX_LEN_LAST_NAME,
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Last name"
            }
        ),
        validators=(
            validators.MinLengthValidator(
                MIN_LEN_LAST_NAME
            ),
            validate_only_letters,
        ),
    )

    phone_number = forms.CharField(
        max_length=MAX_LEN_PHONE,
        label="Phone Number",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Phone number"
            }
        ),
        validators=(
            validate_mobile_number,
            validate_only_numbers,
        ),
    )

    class Meta:
        model = UserModel
        fields = (
            'email',
            'phone_number',
            'first_name',
            'last_name',
        )

    def save(self, commit=True):
        user = super().save(commit=commit)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        phone_number = self.cleaned_data['phone_number']

        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            user=user,
        )
        if commit:
            profile.save()

        return user
