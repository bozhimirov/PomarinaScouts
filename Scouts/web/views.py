from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import generic as views

from Scouts.account_profile.models import Profile
from Scouts.core.utils import get_photo_url
from Scouts.items.models import Item, UsedItem
from Scouts.orders.models import Order

# from Scouts.web.forms import SearchPhotosForm, PhotoCommentForm

UserModel = get_user_model()


class IndexView(views.TemplateView):
    model = UserModel
    template_name = 'index.html'


class SuccessView(views.TemplateView):
    model = UserModel
    template_name = 'core/success.html'


class ContactsView(views.TemplateView):
    model = UserModel
    template_name = 'core/contacts.html'


class ForParentsView(views.TemplateView):
    model = UserModel
    template_name = 'info_for_parents.html'


def scout_store(request):
    all_items = Item.objects.all()
    all_used_items = UsedItem.objects.all()
    count_of_items = all_items.count()
    count_of_used_items = all_used_items.count()
    all_orders = Order.objects.all()
    all_users = Profile.objects.all()
    for_sending = False
    for sent in all_orders:
        if not sent.sent:
            for_sending = True
    received = False
    for rec in all_orders:
        if not rec.received and rec.sent:
            received = True

    context = {
        'for_sending': for_sending,
        'received': received,
        'all_orders': all_orders,
        'all_items': all_items,
        'all_users': all_users,
        'all_used_items': all_used_items,
        'count_of_items': count_of_items,
        'count_of_used_items': count_of_used_items,
    }

    return render(request, template_name='core/marketplace.html', context=context)


def scout_store_new(request):
    all_items = Item.objects.all()
    len_items = len(all_items)
    paginator = Paginator(all_items, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_items': all_items,
        'len_items': len_items,
        'page_obj': page_obj
    }

    return render(request, template_name='core/marketplace-new.html', context=context)


@login_required()
def scout_store_used(request):
    all_used_items = UsedItem.objects.all()
    paginator = Paginator(all_used_items, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_used_items': all_used_items,
        'page_obj': page_obj
    }

    return render(request, template_name='core/marketplace-used.html', context=context)

