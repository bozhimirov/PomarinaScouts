from django.test import TestCase

from Scouts.account_profile.forms import UserEditForm


class ProfileFormTests(TestCase):

    def test_profile_edit_disabled_fields__when_name_disabled__expect_name_disabled(self):
        UserEditForm.disabled_fields = ('first_name',)
        form = UserEditForm()
        disabled_fields = {
            name: field.widget.attrs[UserEditForm.disabled_attr_name]
            for name, field in form.fields.items()
            if UserEditForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            UserEditForm.disabled_attr_name,
            disabled_fields['first_name'],
        )
        self.assertEqual(1, len(disabled_fields))

    def test_profile_edit_disabled_fields__when_all_disabled__expect_all_disabled(self):
        UserEditForm.disabled_fields = '__all__'
        form = UserEditForm()
        disabled_fields = {
            name: field.widget.attrs[UserEditForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            UserEditForm.disabled_attr_name,
            disabled_fields['email'],
        )
        self.assertEqual(
            UserEditForm.disabled_attr_name,
            disabled_fields['phone_number'],
        )
        self.assertEqual(
            UserEditForm.disabled_attr_name,
            disabled_fields['gender'],
        )
        self.assertEqual(
            UserEditForm.disabled_attr_name,
            disabled_fields['first_name'],
        )
        self.assertEqual(
            UserEditForm.disabled_attr_name,
            disabled_fields['last_name'],
        )
        self.assertEqual(
            UserEditForm.disabled_attr_name,
            disabled_fields['profile_image'],
        )

