from django.contrib import admin

from Scouts.kids.models import Kid


@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):

    list_filter = (
        'age',
        'gender',
        'parent_name',
    )

    list_display = (
        'id',
        'first_name',
        'last_name',
        'age',
        'gender',
        'phone_number',
        'parent_phone',
        'parent_name',
    )

    ordering = (
        'users',
    )

