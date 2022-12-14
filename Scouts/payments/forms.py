import operator

from django import forms

from Scouts.core.form_mixins import DisabledFormMixin
from Scouts.payments.models import Payment


class PaymentBaseForm(forms.ModelForm):
    class Meta:
        model = Payment
        ordered = sorted(Payment.objects.all(), key=operator.attrgetter(
            'generated_date',
            'model_name',
        )
                         )
        exclude = (
            'generated_date',
            'tax_per_kid',
            'confirmed_by_user',
            'staff_member',
            'confirmed_manually',
            'paid',
            'slug',
            'parent',
            'period_billed',
            'confirmed_by_staff',
        )


class PaymentCreateForm(PaymentBaseForm):

    comments = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Optional / Comments on payment"
            }
        ),
    )

    class Meta:
        model = Payment
        fields = (
            'model_name',
            'kid',
            'comments',
        )


class PaymentEditForm(PaymentBaseForm):
    class Meta:
        model = Payment
        exclude = (
            'staff_member',
            'parent',
            'generated_date',
            'confirmed_by_user',
            'slug',
            'paid',
            'confirmed_by_staff',
        )


class PaymentConfirmForm(PaymentEditForm):
    class Meta:
        model = Payment
        fields = ()


class PaymentConfirmUserForm(PaymentEditForm):
    class Meta:
        model = Payment
        fields = ()


class PaymentDeleteForm(DisabledFormMixin, PaymentBaseForm):
    disabled_fields = '__all__'

