from django import forms

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.orders.models import Order


class OrderBaseForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = (
            'category',
            'item_name',
            'publication_date',
            'user',
            'item',
            'slug',
            'staff_member',
            'confirmed_by_staff',
            'received_by_user',
            'received',
            'sent',
            'staff_member_finished',
            'additional_comment',
        )


class OrderCreateForm(OrderBaseForm):

    quantity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Required / Please choose quantity of item"
            }
        ),
    )

    comments = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Comments on order"
            }
        ),
    )


class OrderEditForm(OrderBaseForm):

    quantity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Required / Please choose quantity of item"
            }
        ),
    )

    comments = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Comments on order"
            }
        ),
    )

    class Meta:
        model = Order
        exclude = (
            'category',
            'item_name',
            'publication_date',
            'user',
            'slug',
            'staff_member',
            'confirmed_by_staff',
            'received_by_user',
            'received',
            'sent',
            'additional_comment',
            'staff_member_finished',
        )


class OrderSendForm(OrderBaseForm):
    class Meta:
        model = Order
        # fields = ('quantity', 'category', 'item_name', 'ages', 'size', 'gender', 'place_to_deliver', 'comments')
        fields = ()


class OrderReceiveForm(OrderBaseForm):
    additional_comment = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Comments if needed"
            }
        ),
    )

    class Meta:
        model = Order
        fields = (
            'additional_comment',
        )


class OrderDeleteForm(DisabledFormMixin, OrderBaseForm):
    disabled_fields = '__all__'
