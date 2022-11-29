from django import forms
from django.http import request

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.orders.models import Order


class OrderBaseForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('category', 'item_name', 'publication_date', 'user', 'item', 'slug',)


class OrderCreateForm(OrderBaseForm):
    pass


class OrderEditForm(OrderBaseForm):
    class Meta:
        model = Order
        exclude = ('category', 'item_name', 'publication_date', 'user', 'slug',)


class OrderDeleteForm(DisabledFormMixin, OrderBaseForm):
    disabled_fields = '__all__'

    # def save(self, commit=True):
    #     if commit:
    #         # self.instance.tagged_pets.clear()  # many-to-many
    #         #
    #         # Item.objects.all() \
    #         #     .first().tagged_pets.clear()
    #         # PhotoLike.objects.filter(photo_id=self.instance.id) \
    #         #     .delete()  # one-to-many
    #         PhotoComment.objects.filter(photo_id=self.instance.id) \
    #             .delete()  # one-to-many
    #         self.instance.delete()
    #
    #     return self.instance
