from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views import generic as views

from Scouts.account_profile.forms import UserCreateForm
from Scouts.account_profile.models import Profile
from Scouts.payments.models import Payment

UserModel = get_user_model()


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'profile/profile-details.html'
    model = Profile
    payments = Payment.objects.all()

    # '''Made for migrations'''
    # payments = []
    unpaid = False
    for payment in payments:
        if not payment.paid:
            unpaid = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object.user
        context['unpaid'] = self.unpaid

        return context


class EditUserView(LoginRequiredMixin, views.UpdateView):
    template_name = 'profile/profile-edit.html'
    model = Profile
    fields = (
        'first_name',
        'last_name',
        'gender',
        'phone_number',
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

        login(request, self.object)

        return response
