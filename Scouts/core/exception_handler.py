import logging

from django.http import HttpResponse, response
from django.shortcuts import render
from django.template import loader


def custom_handler500(request, *args, **kwargs):

    resp = 'status=500'
    logging.error(
        f'Server error {request} appeared for {request.path}; method: {request.method} with response content: {resp}'
    )
    return render(request, '404.html')


def page_not_found_handler(request, *args, **kwargs):
    logging.error(f"Wrong URL requested; path {request.path}; method: {request.method}")

    return render(request, '404.html')

