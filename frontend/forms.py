from allauth.account.forms import LoginForm, SignupForm
from django import forms


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'})
        self.fields['remember'].widget = forms.PasswordInput(attrs={'class': 'form-check-input'})
        self.fields['remember'].widget = forms.PasswordInput(attrs={'class': 'form-check-input', 'type': 'checkbox'})


class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'})
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'})
        self.fields['password1'].widget = forms.TextInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.TextInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Re-type Password'})
