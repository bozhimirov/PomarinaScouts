from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views import generic as views

from Scouts.account_profile.forms import UserCreateForm
from Scouts.account_profile.models import Profile
from Scouts.accounts.models import AppUser
from Scouts.items.models import UsedItem
from Scouts.kids.models import Kid
from Scouts.orders.models import Order
from Scouts.payments.models import Payment

UserModel = get_user_model()


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'profile/profile-details.html'
    model = Profile
    payments = Payment.objects.all()
    not_received_orders_all = Order.objects.filter(received=False)
    not_received_orders = []
    # Order.objects.filter(user_id=AppUser.objects.filter(pk=self.request.user.pk))

    for order in not_received_orders_all:
        # if order.user == self.object.user:
        pass
    paid_payments = Payment.objects.filter(paid=True)
    items_for_sale = UsedItem.objects.all()
    kids = Kid.objects.all()
    len_kids = len(Kid.objects.all())
    # '''Made for migrations'''
    # payments = []
    # not_received_orders = []
    # paid_payments = []
    # items_for_sale = []
    paid = False
    unpaid = False
    for payment in payments:
        if not payment.paid:
            unpaid = True
        if payment.paid:
            paid = True
    used_items = False
    for item in items_for_sale:
        if item:
            used_items = True
    not_received = False
    for order in not_received_orders:
        if order:
            not_received = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['not_received_orders'] = Order.objects.filter(user_id=self.request.user.pk)
        context['is_owner'] = self.request.user == self.object.user
        context['paid'] = self.paid
        context['unpaid'] = self.unpaid
        context['len_kids'] = self.len_kids
        context['kids'] = self.kids
        context['used_items'] = self.used_items
        context['payments'] = self.payments
        context['paid_payments'] = self.paid_payments
        context['not_received_orders_all'] = self.not_received_orders_all
        context['not_received'] = self.not_received
        context['items_for_sale'] = self.items_for_sale

        return context


class EditUserView(LoginRequiredMixin, views.UpdateView):
    template_name = 'profile/profile-edit.html'
    model = Profile
    fields = (
        'first_name',
        'last_name',
        'phone_number',
        'gender',
        'profile_image',
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object.user

        return context

    def get_success_url(self):
        return reverse_lazy(
            'details user',
            kwargs={
                'pk': self.request.user.pk,
            }
        )


class DeleteUserView(LoginRequiredMixin, views.DeleteView):
    template_name = 'profile/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user.pk == self.object.pk

        return context


class SignUpView(views.CreateView):
    model = Profile
    template_name = 'accounts/register.html'
    form_class = UserCreateForm

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.request.user.pk

        return context

    def get_success_url(self):
        return reverse_lazy('success')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        login(request, self.object)

        return response
