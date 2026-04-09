from django import forms
from .models import UserRegistrationModel


class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'pattern': '^[A-Za-z ]+$',
        'placeholder': 'Full name'
    }), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(attrs={
        'pattern': '^[A-Za-z0-9_]+$',
        'placeholder': 'Login ID (letters, numbers, underscore)'
    }), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
        'title': 'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters',
        'placeholder': 'Password'
    }), required=True, max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(attrs={
        'pattern': '[56789][0-9]{9}',
        'placeholder': '10-digit mobile number'
    }), required=True, max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'email@example.com'
    }), required=True, max_length=100)
    locality = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Locality'}), required=True, max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 22, 'placeholder': 'Address'}), required=True, max_length=250)
    city = forms.CharField(widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'pattern': '[A-Za-z ]+',
        'title': 'Enter Characters Only ',
        'placeholder': 'City'
    }), required=True, max_length=100)
    state = forms.CharField(widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'pattern': '[A-Za-z ]+',
        'title': 'Enter Characters Only ',
        'placeholder': 'State'
    }), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta():
        model = UserRegistrationModel
        fields = '__all__'