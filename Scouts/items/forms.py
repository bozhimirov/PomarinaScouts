from django import forms

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.items.models import Item, UsedItem
# from Scouts.web.models import PhotoComment


class ItemBaseForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('publication_date', 'user', 'slug')


class ItemCreateForm(ItemBaseForm):
    class Meta:
        model = Item
        exclude = ('ages', 'size', 'gender', 'publication_date', 'user', 'slug')


class UsedItemCreateForm(ItemBaseForm):
    class Meta:
        model = UsedItem
        exclude = ('name', 'price', 'publication_date', 'user', 'slug')


class ItemEditForm(ItemBaseForm):
    class Meta:
        model = Item
        exclude = ('ages', 'size', 'gender', 'publication_date', 'user', 'slug')


class UsedItemEditForm(ItemBaseForm):
    class Meta:
        model = UsedItem
        exclude = ('name', 'price', 'publication_date', 'user', 'slug')


class ItemDeleteForm(DisabledFormMixin, ItemBaseForm):
    disabled_fields = '__all__'

    def save(self, commit=True):
        if commit:

            self.instance.delete()

        return self.instance
