from django.contrib import admin

from Scouts.payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'staff_member', 'tax_per_kid', 'period_billed', 'comments', 'generated_date', 'confirmed_by_user', 'kid', 'parent', 'paid')
    list_filter = ('model_name', 'staff_member', 'tax_per_kid', 'period_billed', 'generated_date', 'confirmed_by_user', 'kid', 'parent', 'paid')
