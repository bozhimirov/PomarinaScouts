from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from Scouts.account_profile.forms import UserEditForm, UserCreateForm
from Scouts.account_profile.models import Profile

UserModel = get_user_model()


@admin.register(Profile)
class ProfileAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm

    ordering = ('first_name',)
    list_display = ['first_name', 'last_name', 'phone_number', 'gender', 'user']
    list_filter = ()
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('first_name', 'last_name', 'phone_number', 'gender', 'profile_image'),
            },
        ),
    )
    fieldsets = (
        (None, {'fields': ()}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'gender', 'profile_image', 'user')}),

    )
    filter_horizontal = (

    )


