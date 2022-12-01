from django import forms
from django.contrib.auth import get_user_model
from django.core import validators

from Scouts.account_profile.models import Profile
from Scouts.accounts.forms import AppUserEditForm, AppUserCreationForm
from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.core.model_mixins import Gender
from Scouts.core.validators import validate_only_letters, validate_only_numbers, validate_file_less_than_5mb

UserModel = get_user_model()


class UserEditForm(DisabledFormMixin, AppUserEditForm):
    disabled_fields = ('first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        model = Profile
        fields = '__all__'
        # field_classes = {'username': UsernameField}
        labels = {
            'username': 'Username',
            'phone_number': 'Phone Number',
            'gender': 'Gender',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Upload Your Picture',
        }
        # widgets = {
        #     'username': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Username'
        #         }
        #     ),
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'First Name'
        #         }
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Last Name'
        #         }
        #     ),
        #     'phone_number': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Phone Number'
        #         }
        #     ),
        #     'email': forms.EmailInput(
        #         attrs={
        #             'placeholder': 'Email',
        #         }
        #     ),
        #     'profile_image': forms.FileInput(
        #         attrs={
        #             'placeholder': 'Optional / Upload Your Picture',
        #         }
        #     ),
        #
        # }


class UserCreateForm(AppUserCreationForm):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MIN_LEN_PHONE = 10
    MAX_LEN_PHONE = 10

    first_name = forms.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        help_text="Please use only letters.",
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ),
    )

    last_name = forms.CharField(
        max_length=MAX_LEN_LAST_NAME,
        help_text="Please use only letters.",
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ),
    )

    phone_number = forms.CharField(
        max_length=MAX_LEN_PHONE,
        validators=(
            validators.MinLengthValidator(MIN_LEN_PHONE),
            validate_only_numbers,
        ),
    )

    # gender = forms.CharField(
    #     max_length=Gender.max_len(),
    #     null=True,
    #     blank=True,
    #
    # )
    #
    # profile_image = forms.ImageField(
    #     validators=(validate_file_less_than_5mb,),
    #     null=True,
    #     blank=True,
    # )
    labels = {
        'email': 'Email',
        'phone_number': 'Phone Number',
        'first_name': 'First Name',
        'last_name': 'Last Name',
    }

    # widgets = {
    #     'username': forms.TextInput(
    #         attrs={
    #             'placeholder': 'Username'
    #         }
    #     ),
    #     'first_name': forms.TextInput(
    #         attrs={
    #             'placeholder': 'First Name'
    #         }
    #     ),
    #     'last_name': forms.TextInput(
    #         attrs={
    #             'placeholder': 'Last Name'
    #         }
    #     ),
    #     'phone_number': forms.TextInput(
    #         attrs={
    #             'placeholder': 'Phone Number'
    #         }
    #     ),
    #     'email': forms.EmailInput(
    #         attrs={
    #             'placeholder': 'Email',
    #         }
    #     ),
    #     'profile_image': forms.FileInput(
    #         attrs={
    #             'placeholder': 'Optional / Upload Your Picture',
    #         }
    #     ),
    #
    # }

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