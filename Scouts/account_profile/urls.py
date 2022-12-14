from django.urls import path, include

from Scouts.account_profile.views import UserDetailsView, EditUserView, DeleteUserView, SignUpView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
    path('profile/<int:pk>/', include(
        [
            path('', UserDetailsView.as_view(), name='details user'),
            path('edit/', EditUserView.as_view(), name='edit user'),
            path('delete/', DeleteUserView.as_view(), name='delete user'),
        ]
    )
         ),

)
