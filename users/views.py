from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, TemplateView
from users.models import User
from users.fotms import UserForm, ProfileForm
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password


class LoginView(BaseLoginView):
    
    template_name = 'users/login.html'


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('catalog:index')


class RegisterView(CreateView):
    
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        
        response = super().form_valid(form)
        new_user = form.save()
        new_user.is_active = False
        new_user.save()
        
        code = new_user.password
        email =  new_user.email
        current_site = get_current_site(self.request)
        
        send_mail(
            'Верификация',
            f'Перейдите по ссылке для верификации: http://{current_site.domain}/users/verification/?source={code}&email={email}',
            EMAIL_HOST_USER,
            [new_user.email]
        )
        
        return response


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RecoveryUpdateView(TemplateView):
    # form_class = RecoveryForm
    template_name = 'users/recovery.html'
    success_url = reverse_lazy('users:login')
    
    def post(self, request):
        email =request.POST.get('email_recovery', '')
        if email != '':
            try:
                user = User.objects.get(email=email)
                new_password = User.objects.make_random_password()
                hash_new_password = make_password(new_password)
                user.password = hash_new_password
                user.save()
                send_mail(
                    'Смена пароля',
                    f'Ваш новый пароль для авторизации: {new_password}',
                    EMAIL_HOST_USER,
                    [user.email]
                )
            except:
                pass    
        return redirect('users:login')


class VerificationView(View):
    
    def get(self, request):
        
        source = request.GET.get('source', '')
        email = request.GET.get('email', '')
        
        try:
            user = User.objects.get(email=email) 
            if user.password == source:
                user.is_active = True
                user.save()      
        except:      
            pass

        return redirect('users:login')
