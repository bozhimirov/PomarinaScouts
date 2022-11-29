from django.contrib.auth import get_user_model
from django.db import models

from Scouts.items.models import Item

UserModel = get_user_model()

#
# class Bank(models.Model):
#
#     name_of_receiver = models.CharField(
#         default='Pomarina Scouts NPO',
#         max_length=len('Pomarina Scouts NPO')
#
#     )
#
#     iban_receiver = models.CharField(
#         default='BG00PSO80009000100010',
#         max_length=len('BG00PSO80009000100010')
#     )
#
#     bic_receiver = models.CharField(
#         default='PSOBGSF',
#         max_length=len('PSOBGSF')
#     )
#
#     bank_name_receiver = models.CharField(
#         default='Pomarina Scouts Bank LTD',
#         max_length=len('Pomarina Scouts Bank LTD')
#     )

#
# class PhotoComment(models.Model):
#     MAX_TEXT_LENGTH = 300
#     text = models.TextField(
#         max_length=MAX_TEXT_LENGTH,
#         null=False,
#         blank=False,
#     )
#
#     publication_date_and_time = models.DateTimeField(
#         auto_now_add=True,
#         null=False,
#         blank=True,
#     )
#
#     to_photo = models.ForeignKey(
#         Item,
#         on_delete=models.RESTRICT,
#         null=False,
#         blank=True,
#     )
#     user = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE,
#     )
#
#     class Meta:
#         ordering = ["-publication_date_and_time"]
#
# #
# class PhotoLike(models.Model):
#     # Photo's field for likes is named `{NAME_OF_THIS_MODEL.lower()}_set`
#     to_photo = models.ForeignKey(
#         Item,
#         on_delete=models.CASCADE,
#         null=False,
#         blank=True,
#     )
