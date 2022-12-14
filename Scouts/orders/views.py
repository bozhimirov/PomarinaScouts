import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.utils import timezone

from Scouts.account_profile.models import Profile
from Scouts.items.models import Item
from Scouts.orders.forms import OrderCreateForm, OrderEditForm, OrderSendForm, OrderReceiveForm
from Scouts.orders.models import Order
from Scouts.orders.signals import send_email_on_successful_order

UserModel = get_user_model()


@login_required
def details_order(request, pk):
    order = Order.objects.filter(pk=pk).get()
    user = UserModel.objects.get(pk=order.user_id)
    all_users = Profile.objects.all()

    context = {
        'order': order,
        'is_owner': request.user == order.user,
        'user': user,
        'all_users': all_users,
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
            form.save()

            return redirect('details order', pk=order.pk)
    # send_email_on_successful_order(UserModel, )
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


@login_required
def send_order(request, pk):
    order = Order.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = OrderSendForm(instance=order)
    else:
        form = OrderSendForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.confirmed_by_staff = timezone.now()
            order.sent = True
            order.staff_member = request.user.pk
            order.save()
            form.save()

            return redirect('scout store')

    context = {
        'form': form,
        'pk': pk,
        'order': order,
        'is_owner': order.staff_member == request.user,
    }

    return render(
        request,
        'orders/order-sent.html',
        context,
    )


@login_required
def receive_order(request, pk):
    order = Order.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = OrderReceiveForm(instance=order)
    else:
        form = OrderReceiveForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.received_by_user = timezone.now()
            order.received = True
            order.staff_member_finished = request.user.pk
            order.save()
            form.save()

            return redirect('scout store')

    context = {
        'form': form,
        'pk': pk,
        'order': order,
        'is_owner': order.staff_member == request.user,
    }

    return render(
        request,
        'orders/order-received.html',
        context,
    )

