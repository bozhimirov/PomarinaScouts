from django import forms
from django.http import request

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.orders.models import Order


class OrderBaseForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = (
            'category', 'item_name', 'publication_date', 'user', 'item', 'slug', 'staff_member', 'confirmed_by_staff',
            'received_by_user', 'received', 'sent', 'staff_member_finished')


class OrderCreateForm(OrderBaseForm):
    pass


class OrderEditForm(OrderBaseForm):
    class Meta:
        model = Order
        exclude = ('category', 'item_name', 'publication_date', 'user', 'slug', 'staff_member', 'confirmed_by_staff',
                   'received_by_user', 'received', 'sent')


class OrderSendForm(OrderBaseForm):
    class Meta:
        model = Order
        fields = ()


class OrderReceiveForm(OrderBaseForm):
    additional_comment = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Comments if needed"}),
    )

    class Meta:
        model = Order
        fields = ('additional_comment',)


class OrderDeleteForm(DisabledFormMixin, OrderBaseForm):
    disabled_fields = '__all__'
