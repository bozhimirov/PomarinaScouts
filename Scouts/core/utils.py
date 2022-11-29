from datetime import date


def megabytes_to_bytes(mb):
    return mb * 1024 * 1024


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def calculate_month(today):
    today = date.today()
    return f'{today.month - 1} {today.year}'


def calculate_year(today):
    today = date.today()
    return today.year + 1


def kids_info(parent):
    kids_list = []
    for kid in parent.kid_set.all():
        kids_list.append(kid)

    return kids_list
