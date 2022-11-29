from django.contrib.auth import views, get_user_model
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from Scouts.account_profile.models import Profile
from Scouts.items.forms import ItemCreateForm, ItemEditForm, ItemDeleteForm, UsedItemCreateForm, UsedItemEditForm
from Scouts.items.models import Item, UsedItem

UserModel = get_user_model()


def details_item(request, pk):
    item = Item.objects.filter(pk=pk).get()
    category = item.category
    name = item.name
    # comments = item.photocomment_set.all()

    context = {
        'item': item,
        'is_owner': request.user == item.user,
        'category': category,
        'name': name,
        # 'comments': comments,
    }

    return render(
        request,
        'items/item-details.html',
        context,
    )


def details_used_item(request, pk):
    item = UsedItem.objects.filter(pk=pk).get()
    category = item.category
    # comments = item.photocomment_set.all()

    context = {
        'item': item,
        'is_owner': request.user == item.user,
        'category': category,
        # 'comments': comments,
    }

    return render(
        request,
        'used_items/used_item-details.html',
        context,
    )


def get_post_item_form(request, form, success_url, template_path, pk=None):
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
def add_item(request):
    if request.method == 'GET':
        form = ItemCreateForm()
    else:
        form = ItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            form.save_m2m()

            return redirect('details item', pk=item.pk)

    context = {
        'form': form,
    }

    return render(
        request,
        'items/item-create.html',
        context,
    )


@login_required
def add_used_item(request):
    if request.method == 'GET':
        form = UsedItemCreateForm()
    else:
        form = UsedItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            form.save_m2m()

            return redirect('details used item', pk=item.pk)

    context = {
        'form': form,
    }

    return render(
        request,
        'used_items/used_item-create.html',
        context,
    )


@login_required
def edit_item(request, pk):
    item = Item.objects.filter(pk=pk).get()
    # return get_post_item_form(
    #     request,
    #     ItemEditForm(request.POST or None, instance=item),
    #     success_url=reverse_lazy('details item', pk=item.pk),
    #     template_path='items/payment-edit.html',
    #     pk=item.pk,
    # )
    if request.method == 'GET':
        form = ItemEditForm(instance=item)
    else:
        form = ItemEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            # item = form.save(commit=False)
            # item.user = request.user
            # item.save()
            form.save()

            return redirect('details item', pk=item.pk)

    context = {
        'form': form,
        'pk': pk,
        'is_owner': item.user == request.user,
    }

    return render(
        request,
        'items/item-edit.html',
        context,
    )


@login_required
def edit_used_item(request, pk):
    item = UsedItem.objects.filter(pk=pk).get()
    # return get_post_item_form(
    #     request,
    #     ItemEditForm(request.POST or None, instance=item),
    #     success_url=reverse_lazy('details item', pk=item.pk),
    #     template_path='items/payment-edit.html',
    #     pk=item.pk,
    # )
    if request.method == 'GET':
        form = UsedItemEditForm(instance=item)
    else:
        form = UsedItemEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            # item = form.save(commit=False)
            # item.user = request.user
            # item.save()
            form.save()

            return redirect('details used item', pk=item.pk)

    context = {
        'form': form,
        'pk': pk,
        'is_owner': item.user == request.user,
    }

    return render(
        request,
        'used_items/used_item-edit.html',
        context,
    )


@login_required
def delete_item(request, pk):
    item = Item.objects.filter(pk=pk).get()
    item.delete()

    return redirect('details user', request.user.pk)


@login_required
def delete_used_item(request, pk):
    item = UsedItem.objects.filter(pk=pk).get()
    item.delete()

    return redirect('details user', request.user.pk)


@login_required
def contact_seller(request, pk):
    item = UsedItem.objects.filter(pk=pk).get()
    profile_pk = item.user.pk
    user = Profile.objects.filter(pk=profile_pk).get()

    context = {
        'item': item,
        'user': user,
    }

    return render(
        request,
        'used_items/contact_seller.html',
        context,
    )
