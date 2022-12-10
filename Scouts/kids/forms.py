from django import forms
from django.core import validators
from django.db import IntegrityError

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.core.model_mixins import Gender
from Scouts.core.validators import validate_file_less_than_5mb, validate_only_numbers, validate_birth_credentials, \
    validate_age, validate_mobile_number
from Scouts.kids.models import Kid


class KidBaseForm(forms.ModelForm):
    MAX_NAME = 30
    MIN_NAME = 3
    MIN_LEN_PHONE = 10
    MAX_LEN_PHONE = 10

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Required / First Name"
            }
        ),
        validators=(
            validators.MinLengthValidator(MIN_NAME),
        )
    )

    last_name = forms.CharField(
        required=False,
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Optional / Last Name"
            }
        ),
        validators=(
            validators.MinLengthValidator(MIN_NAME),
        )
    )

    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Required / Please use format YYYY-MM-DD:"
            }
        ),
        validators=(
            validate_birth_credentials,
        ),
        error_messages={
            'required': 'Place enter correct birth credentials'
        },

    )

    profile_picture = forms.ImageField(
        required=False,
        label='Profile Picture',
        help_text='Optional / Upload Profile Picture',
        validators=(
            validate_file_less_than_5mb,
        ),
    )

    phone_number = forms.CharField(
        required=False,
        label='Phone Number',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Optional / Kid's Personal Phone Number"
            }
        ),
        validators=(
            validate_mobile_number,
            validate_only_numbers,
        ),
    )

    class Meta:
        MAX_NAME = 30
        MIN_NAME = 3
        MIN_LEN_PHONE = 10
        MAX_LEN_PHONE = 10

        model = Kid
        fields = ('first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'profile_picture')


class KidCreateForm(KidBaseForm):
    pass


class KidEditForm(DisabledFormMixin, KidBaseForm):
    # disabled_fields = ('first_name', 'date_of_birth', 'gender')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        model = Kid
        fields = ('first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'profile_picture')


class KidDeleteForm(DisabledFormMixin, KidBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
