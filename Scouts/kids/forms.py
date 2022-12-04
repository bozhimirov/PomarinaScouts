from django import forms

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.kids.models import Kid


class KidBaseForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ('first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'profile_picture')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender',
            'phone_number': 'Phone Number',
            'profile_picture': 'Profile Picture',
        }


class KidCreateForm(KidBaseForm):
    pass


class KidEditForm(DisabledFormMixin, KidBaseForm):
    disabled_fields = ('first_name',)

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
