
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views, get_user_model

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    model = UserModel
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('details user')

    def get_success_url(self):
        return reverse_lazy(
            'details user',
            kwargs={
                'pk': self.request.user.pk,
            }
        )


class SignOutView(auth_views.LogoutView):
    model = UserModel
    next_page = reverse_lazy('index')
