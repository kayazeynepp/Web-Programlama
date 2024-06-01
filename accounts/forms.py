from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'role', 'password1', 'password2')
        labels = {'role': 'Role'}
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)


class CustomAuthenticationForm(AuthenticationForm):
    pass


class FirebaseLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
