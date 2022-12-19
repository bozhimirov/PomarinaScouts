from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from django.views import generic as views

from Scouts.account_profile.forms import UserCreateForm
from Scouts.account_profile.models import Profile
from Scouts.items.models import UsedItem
from Scouts.kids.models import Kid
from Scouts.orders.models import Order
from Scouts.payments.models import Payment

UserModel = get_user_model()


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'profile/profile-details.html'
    model = Profile

    payments_paginate_by = 2
    payments = Payment.objects.order_by('-generated_date')
    orders = Order.objects.all()
    items_for_sale = UsedItem.objects.order_by('publication_date')
    kids = Kid.objects.order_by('-age')
    not_received_orders_all = orders.filter(received=False)
    not_received_orders_ordered = not_received_orders_all.order_by('publication_date')

    # '''Made for migrations'''
    # payments = []
    # orders = []
    # items_for_sale = []

    def get_payments_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_payments(self):
        page = self.get_payments_page()
        self_pk = self.request.user.pk
        paid_payments_unordered = self.payments.filter(paid=True)
        paid_payments = paid_payments_unordered.order_by('-confirmed_by_staff')
        self_payments = paid_payments.filter(parent_id=self_pk)

        paginator = Paginator(self_payments, self.payments_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['is_owner'] = self.request.user == self.object.user
        context['self_payments'] = self.get_paginated_payments()
        context['not_received_orders_self'] = self.not_received_orders_all.filter(user_id=self.request.user)
        context['items_for_sale'] = self.items_for_sale.filter(user_id=self.request.user.pk)
        context['kids'] = self.kids.filter(users_id=self.request.user.pk)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.request.user.pk
        return context

    def get_success_url(self):
        return reverse_lazy('success')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:
            login(request, self.object)

        return response
