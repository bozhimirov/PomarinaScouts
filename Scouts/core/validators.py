from datetime import date

from django.core import exceptions

from Scouts.core.utils import megabytes_to_bytes


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed!')


def validate_gt_zero(value):
    if not value >= 1:
        raise exceptions.ValidationError('Quantity must not be zero!')


def validate_only_numbers(value):
    for ch in value:
        if not ch.isdigit():
            raise exceptions.ValidationError('Only numbers are allowed!')


def validate_mobile_number(value):
    if len(value) != 10:
        raise exceptions.ValidationError('Place phone number in format: 0987654321')


def validate_file_less_than_5mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise exceptions.ValidationError(f'Max file size is {megabyte_limit}MB')


def validate_birth_credentials(born):
    today = date.today()

    if 4 > (today.year - born.year) or (today.year - born.year) > 26:
        raise exceptions.ValidationError(f'Invalid year declared')
    if 1 > born.month or born.month > 12:
        raise exceptions.ValidationError(f'Invalid month declared')
    if 1 > born.day or born.day > 31:
        raise exceptions.ValidationError(f'Invalid day declared')


def validate_age(age):
    if 3 > age or age > 26:
        raise exceptions.ValidationError(f'Invalid age declared')
