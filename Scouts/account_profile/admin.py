from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from Scouts.account_profile.forms import UserCreateForm
from Scouts.account_profile.models import Profile

UserModel = get_user_model()


@admin.register(Profile)
class ProfileAdmin(auth_admin.UserAdmin):
    add_form = UserCreateForm

    ordering = (
        'user',
    )

    list_display = (
        'user',
        'first_name',
        'last_name',
        'phone_number',
        'gender'
    )

    list_filter = (
        'last_name',
        'gender'
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'first_name',
                    'last_name',
                    'phone_number',
                    'gender',
                    'profile_image',
                ),
            },
        ),
    )
    fieldsets = (
        (None,
         {
             'fields': ()
         }
         ),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'phone_number',
                    'gender',
                    'profile_image',
                )
            }
        ),
    )
    filter_horizontal = (

    )


