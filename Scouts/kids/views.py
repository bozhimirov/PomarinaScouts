from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from Scouts.kids.forms import KidCreateForm, KidEditForm, KidDeleteForm
from django.contrib.auth import get_user_model

from Scouts.kids.utils import get_kid_by_name_and_id

UserModel = get_user_model()


@login_required
def details_kid(request, uid, kid_slug):
    kid = get_kid_by_name_and_id(kid_slug, uid)

    context = {
        'kid': kid,
        'is_owner': kid.users == request.user,
        'uid': uid,
        'kid_slug': kid_slug,
    }

    return render(
        request,
        'kids/kids-details.html',
        context,
    )


@login_required
def add_kid(request):
    if request.method == 'GET':
        form = KidCreateForm()
    else:
        form = KidCreateForm(request.POST, request.FILES)
        if form.is_valid():
            kid = form.save(commit=False)
            kid.users = request.user
            try:
                kid.save()
                return redirect('details user', pk=request.user.pk)
            except IntegrityError as e:
                messages.error(request, 'Integrity error.' + str(e))
                return HttpResponseRedirect(reverse('add kid', ))

        # form = KidCreateForm()
    context = {
        'form': form,

    }

    return render(request, 'kids/kids-create.html', context)


@login_required
def edit_kid(request, uid, kid_slug):
    kid = get_kid_by_name_and_id(kid_slug, uid)

    if request.method == 'GET':
        form = KidEditForm(instance=kid)
    else:
        form = KidEditForm(request.POST, request.FILES, instance=kid)
        if form.is_valid():
            form.save()
            return redirect('details kid', uid=uid, kid_slug=kid_slug)

    context = {
        'form': form,
        'kid_slug': kid_slug,
        'uid': uid,
        'is_owner': kid.users == request.user,
    }

    return render(
        request,
        'kids/kids-edit.html',
        context,
    )


@login_required
def delete_kid(request, uid, kid_slug):
    kid = get_kid_by_name_and_id(kid_slug, uid)

    if request.method == 'GET':
        form = KidDeleteForm(instance=kid)
    else:
        form = KidDeleteForm(request.POST, instance=kid)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
        'kid_slug': kid_slug,
        'uid': uid,
    }

    return render(
        request,
        'kids/kids-delete.html',
        context,
    )
