from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField
from django.core import validators

from Scouts.account_profile.models import Profile
from Scouts.accounts.forms import AppUserEditForm, AppUserCreationForm
from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.core.model_mixins import Gender
from Scouts.core.validators import validate_only_letters, validate_only_numbers, validate_file_less_than_5mb, \
    validate_mobile_number

UserModel = get_user_model()


class UserEditForm(DisabledFormMixin, AppUserEditForm):
    disabled_fields = ('first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'email': 'Email',
            'phone_number': 'Phone Number',
            'gender': 'Gender',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Upload Your Picture',
        }


class UserCreateForm(AppUserCreationForm):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_PHONE = 10

    first_name = forms.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        widget=forms.TextInput(
            attrs={'placeholder': "First name"}),
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ),
    )

    last_name = forms.CharField(
        max_length=MAX_LEN_LAST_NAME,
        widget=forms.TextInput(
            attrs={'placeholder': "Last name"}),
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ),
    )

    phone_number = forms.CharField(
        max_length=MAX_LEN_PHONE,
        widget=forms.TextInput(
            attrs={'placeholder': "Phone number"}),
        validators=(
            validate_mobile_number,
            validate_only_numbers,
        ),
    )

    class Meta:
        model = UserModel
        fields = ('email', 'phone_number', 'first_name', 'last_name',)

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
