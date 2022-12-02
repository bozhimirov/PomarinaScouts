from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models.functions import datetime
from django.shortcuts import render, redirect

from Scouts.account_profile.models import Profile
from Scouts.core.model_mixins import PaymentType, TaxType
from Scouts.core.utils import kids_info, calculate_month, calculate_year
from Scouts.payments.forms import PaymentCreateForm, PaymentEditForm, PaymentConfirmForm
from Scouts.payments.models import Payment

UserModel = get_user_model()


@login_required
def details_payment(request, pk):
    payment = Payment.objects.filter(pk=pk).get()
    user = UserModel.objects.get(pk=payment.parent_id)

    context = {
        'payment': payment,
        'is_owner': request.user == payment.parent,
        'user': user,
    }

    return render(
        request,
        'payments/payment-details.html',
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
def add_payment(request):
    current_user_pk = request.user.pk
    user = Profile.objects.get(pk=current_user_pk)

    payment_set = Payment.objects.filter(staff_member=user.get_full_name())
    if request.method == 'GET':
        form = PaymentCreateForm()

    else:
        form = PaymentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.staff_member = user.get_full_name()

            payment.parent = payment.kid.users
            payment.period_billed = calculate_month(payment.generated_date)

            if payment.model_name == 'MonthlyTax':

                payment.period_billed = calculate_month(payment.generated_date)
                kids_list = kids_info(payment.kid.users)
                if not payment.kid == kids_list[0]:
                    payment.tax_per_kid = payment.MONTHLY_TAX / 2
                else:
                    payment.tax_per_kid = payment.MONTHLY_TAX

            elif payment.model_name == 'AnnualFee':
                payment.tax_per_kid = payment.ANNUAL_TAX

                payment.period_billed = calculate_year(payment.generated_date)

            payment.save()
            form.save()

            return redirect('add payment')

    context = {
        'form': form,
        'payment_set': payment_set

    }

    return render(
        request,
        'payments/payment-create.html',
        context,
    )


@login_required
def edit_payment(request, pk):
    payment = Payment.objects.filter(pk=pk).get()
    user = UserModel.objects.get(pk=payment.parent_id)

    if request.method == 'GET':
        form = PaymentEditForm(instance=payment)
    else:
        form = PaymentEditForm(request.POST, request.FILES, instance=payment)
        if form.is_valid():
            # item = form.save(commit=False)
            # item.user = request.user
            # item.save()
            form.save()

            return redirect('add payment')

    context = {
        'form': form,
        'pk': pk,
        'user': user,
        'payment': payment,
        'is_owner': payment.staff_member == request.user,
    }

    return render(
        request,
        'payments/payment-edit.html',
        context,
    )


@login_required
def confirm_payment(request, pk):
    payment = Payment.objects.filter(pk=pk).get()
    user = UserModel.objects.get(pk=payment.parent_id)

    if request.method == 'GET':
        form = PaymentConfirmForm(instance=payment)
    else:
        form = PaymentConfirmForm(request.POST, request.FILES, instance=payment)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.confirmed_by_user = datetime.datetime.now()
            payment.save()
            form.save()

            return redirect('details user', pk=user.pk)

    context = {
        'form': form,
        'pk': pk,
        'user': user,
        'payment': payment,
        'is_owner': payment.staff_member == request.user,
    }

    return render(
        request,
        'payments/payment-confirm.html',
        context,
    )


@login_required
def confirm_payment_by_staff(request, pk):
    payment = Payment.objects.filter(pk=pk).get()
    staff_user = UserModel.objects.get(pk=request.user.pk)

    if request.method == 'GET':
        form = PaymentConfirmForm(instance=payment)
    else:
        form = PaymentConfirmForm(request.POST, request.FILES, instance=payment)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.confirmed_by_staff = datetime.datetime.now()
            payment.paid = True
            payment.save()
            form.save()

            return redirect('add payment')

    context = {
        'form': form,
        'pk': pk,
        'staff_user': staff_user,
        'payment': payment,
        'is_owner': payment.staff_member == request.user,
    }

    return render(
        request,
        'payments/payment-confirm-staff.html',
        context,
    )


@login_required
def delete_payment(request, pk):
    payment = Payment.objects.filter(pk=pk).get()
    payment.delete()

    return redirect('add payment')
