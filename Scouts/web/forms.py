from django import forms

from Scouts.web.models import Bank


# from Scouts.web.models import PhotoComment


# class PhotoCommentForm(forms.ModelForm):
#     class Meta:
#         model = PhotoComment
#         fields = ('text',)
#         widgets = {
#             'text': forms.Textarea(
#                 attrs={
#                     'cols': 40,
#                     'rows': 10,
#                     'placeholder': 'Add comment...'
#                 },
#             ),
#         }

#
# class SearchPhotosForm(forms.Form):
#     pet_name = forms.CharField(
#         max_length=50,
#         required=False,
#     )
#
# class BankDetailsForm(forms.Form):
#     class Meta:
#         model = Bank
#
