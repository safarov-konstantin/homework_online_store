from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from catalog.forms import StyleFormMixin
from users.models import User


class UserForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class RecoveryForm(StyleFormMixin, forms.Form):
    email = forms.EmailField(label='Email')


class ProfileForm(StyleFormMixin, UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

    class Meta:
        model = User
        fields = (
            'email', 
            'password', 
            'first_name', 
            'last_name', 
            'avatar', 
            'country', 
            'phone',
        ) 
