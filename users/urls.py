from django.urls import path
from users.apps import UsersConfig
from users.views import (LoginView, LogoutView, RegisterView, 
                         VerificationView, ProfileView, RecoveryUpdateView)


app_name = UsersConfig.name


urlpatterns = [
   path('', LoginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('register/', RegisterView.as_view(), name='register'),
   path('verification/', VerificationView.as_view(), name='verification'),
   path('profile/', ProfileView.as_view(), name='profile'),
   path('recovery/', RecoveryUpdateView.as_view(), name='recovery')

]
