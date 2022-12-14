from django.test import TestCase

from Scouts.kids.forms import KidEditForm


class KidsFormTests(TestCase):

    def test_kid_edit_disabled_fields__when_name_disabled__expect_name_disabled(self):
        KidEditForm.disabled_fields = ('first_name',)
        form = KidEditForm()
        disabled_fields = {
            name: field.widget.attrs[KidEditForm.disabled_attr_name]
            for name, field in form.fields.items()
            if KidEditForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            KidEditForm.disabled_attr_name,
            disabled_fields['first_name'],
        )
        self.assertEqual(1, len(disabled_fields))

    def test_kid_edit_disabled_fields__when_name_date_gender_disabled__expect_3_disabled(self):
        KidEditForm.disabled_fields = (
            'first_name',
            'date_of_birth',
            'gender'
        )
        form = KidEditForm()
        disabled_fields = {
            name: field.widget.attrs[KidEditForm.disabled_attr_name]
            for name, field in form.fields.items()
            if KidEditForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            KidEditForm.disabled_attr_name,
            disabled_fields['first_name'],
        )

        self.assertEqual(
            KidEditForm.disabled_attr_name,
            disabled_fields['date_of_birth'],
        )

        self.assertEqual(
            KidEditForm.disabled_attr_name,
            disabled_fields['gender'],
        )

        self.assertEqual(3, len(disabled_fields))

