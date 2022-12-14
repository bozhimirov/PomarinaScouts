from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from Scouts.orders.models import Order

UserModel = get_user_model()


@receiver(signal=post_save, sender=Order)
def send_email_on_successful_order(instance,  **kwargs):
    pass
    # send_mail(
    #     subject='You made an order!',
    #     message='You made an Order!',
    #     from_email=None,
    #     recipient_list=(instance.user.email,),
    # )
