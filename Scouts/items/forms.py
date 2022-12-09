from django import forms

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.items.models import Item, UsedItem


class ItemBaseForm(forms.ModelForm):
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Location of the Item"
            }
        ),
    )

    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Description of the Item"
            }
        ),
    )

    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Name of the Item"
            }
        ),
    )

    # consider Float-field if necessary for price
    price = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Price of the Item"
            }
        ),
    )

    class Meta:
        model = Item
        exclude = (
            'publication_date',
            'user',
            'slug',
            'location',
        )


class ItemCreateForm(ItemBaseForm):
    class Meta:
        model = Item
        exclude = (
            'ages',
            'size',
            'gender',
            'publication_date',
            'user',
            'slug',
        )


class ItemEditForm(ItemBaseForm):
    class Meta:
        model = Item
        exclude = (
            'ages',
            'size',
            'gender',
            'publication_date',
            'user',
            'slug',
        )


class ItemDeleteForm(DisabledFormMixin, ItemBaseForm):
    disabled_fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class UsedItemBaseForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Description of the Item"
            }
        ),
    )

    location = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Location of the Item"
            }
        ),
    )

    class Meta:
        model = UsedItem
        exclude = (
            'publication_date',
            'user',
            'slug',
        )


class UsedItemCreateForm(UsedItemBaseForm):
    class Meta:
        model = UsedItem
        exclude = (
            'name',
            'price',
            'publication_date',
            'user',
            'slug',
        )


class UsedItemEditForm(UsedItemBaseForm):
    class Meta:
        model = UsedItem
        exclude = (
            'name',
            'price',
            'publication_date',
            'user',
            'slug',
        )


class UsedItemDeleteForm(DisabledFormMixin, UsedItemBaseForm):
    disabled_fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

