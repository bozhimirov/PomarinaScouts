from django.db.models import signals
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from Scouts.account_profile.models import Profile
from Scouts.kids.models import Kid


@receiver(signals.post_save, sender=Profile)
def change_credentials_on_change_profile(instance, sender, **kwargs):
    user = Profile.objects.filter(pk=instance.pk).get()
    self_kids = Kid.objects.filter(users_id=instance.pk)
    for kid in self_kids:
        if kid.users.pk == instance.pk:
            if not kid.parent_phone == user.phone_number:
                kid.parent_phone = user.phone_number
                kid.save()

            if not kid.parent_name == user.get_full_name():
                kid.parent_name = user.get_full_name()
                kid.save()
