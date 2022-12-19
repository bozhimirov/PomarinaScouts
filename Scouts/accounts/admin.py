from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from Scouts.accounts.forms import AppUserCreationForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):

    add_form = AppUserCreationForm
    exclude = (
        'username',
    )

    ordering = (
        '-is_staff',
        '-is_active',
        'id'
    )

    list_display = (
        'email',
        'date_joined',
        'last_login'
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'email',
                    'password1',
                    'password2'
                ),
            },
        ),

    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',)}
         ),

        ('Important dates', {'fields': (
             'last_login',
             'date_joined'
         )}),
    )


USERNAME_FIELD = 'email'

