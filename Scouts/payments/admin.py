from django.contrib import admin

from Scouts.payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'paid',
        'model_name',
        'tax_per_kid',
        'period_billed',
        'generated_date',
        'confirmed_by_user',
        'kid',
        'parent',
        'staff_member',
        'comments',
    )
    list_filter = (
        'confirmed_by_user',
        'paid',
        'model_name',
        'period_billed',
        'generated_date',
        'kid',
        'parent',
        'tax_per_kid',
        'staff_member',
    )
    ordering = (
        'paid',
        '-confirmed_by_user',
        'generated_date',
        'parent',
        'model_name',
    )
