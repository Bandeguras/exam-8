from django.urls import path

from account.views import RegisterView, UserDetailView, UserChangeView, UserChangePasswordView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('update/', UserChangeView.as_view(), name='update'),
    path('password/', UserChangePasswordView.as_view(), name='password_change'),
]