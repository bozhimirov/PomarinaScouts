from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect

from Scouts.items.models import Item, UsedItem
from Scouts.orders.forms import OrderCreateForm, OrderEditForm
from Scouts.orders.models import Order

UserModel = get_user_model()


@login_required
def details_order(request, pk):
    order = Order.objects.filter(pk=pk).get()
    user = UserModel.objects.get(pk=order.user_id)

    context = {
        'order': order,
        'is_owner': request.user == order.user,
        'user': user,
    }

    return render(
        request,
        'orders/order-details.html',
        context,
    )


def get_post_order_form(request, form, success_url, template_path, pk=None):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_path, context)


@login_required
def add_order(request, pk):
    item = Item.objects.filter(pk=pk).get()
    user = request.user
    category = item.category
    name = item.name
    if request.method == 'GET':
        form = OrderCreateForm()

    else:
        form = OrderCreateForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.category = item.category
            order.item_name = item.name
            order.user = request.user
            order.save()
            # form.save_m2m()
            form.save()

            return redirect('details order', pk=order.pk)

    context = {
        'form': form,
        'item': item,
        'user': user,
        'category': category,
        'name': name,

    }

    return render(
        request,
        'orders/order-create.html',
        context,
    )


@login_required
def edit_order(request, pk):
    order = Order.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = OrderEditForm(instance=order)
    else:
        form = OrderEditForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            # item = form.save(commit=False)
            # item.user = request.user
            # item.save()
            form.save()

            return redirect('details order', pk=order.pk)

    context = {
        'form': form,
        'pk': pk,
        'is_owner': order.user == request.user,
    }

    return render(
        request,
        'orders/order-edit.html',
        context,
    )


@login_required
def delete_order(request, pk):
    order = Order.objects.filter(pk=pk).get()
    order.delete()

    return redirect('scout store')
