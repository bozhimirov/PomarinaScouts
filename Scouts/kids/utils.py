from datetime import date

from Scouts.kids.models import Kid


def get_kid_by_name_and_id(kid_slug, uid):
    return Kid.objects.filter(slug=kid_slug, users__id=uid).get()

