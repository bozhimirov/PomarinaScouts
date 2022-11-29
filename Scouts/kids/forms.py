from django import forms

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.kids.models import Kid


# `ModelForm` and `Form`:
# - `ModelForm` binds to models
# - `Form` is detached from models

class KidBaseForm(forms.ModelForm):
    class Meta:
        model = Kid
        # fields = '__all__' (not the case, we want to skip `slug`
        fields = ('first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'profile_picture')
        # exclude = ('slug',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender',
            'phone_number': 'Phone Number',
            'profile_picture': 'Profile Picture',
        }
        # widgets = {
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
        #     'date_of_birth': forms.DateInput(
        #         attrs={
        #             'placeholder': 'mm/dd/yyyy',
        #             'type': 'date',
        #         }
        #     ),
        #
        # }


class KidCreateForm(KidBaseForm):
    pass


class KidEditForm(DisabledFormMixin, KidBaseForm):
    # disabled_fields = ('first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class KidDeleteForm(DisabledFormMixin, KidBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
