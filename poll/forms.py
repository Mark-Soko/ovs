from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import fields

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'username',
        'id':'login__username',
        'autocomplete':'username',
        'placeholder':'Username'
    }),label ='Username')
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'first_name',
        'id':'first_name',
        'autocomplete':'first_name',
        'placeholder':'First name'
    }),label ='First name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'last_name',
        'id':'last_name',
        'autocomplete':'last_name',
        'placeholder':'Last name'
    }),label ='Last name')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'email',
        'id':'email',
        'autocomplete':'email',
        'placeholder':'Email'
    }),label ='Email')
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'password',
        'name':'password',
        'id':'password',
        'autocomplete':'password',
        'placeholder':'Password'
    }),label ='Password')
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'password',
        'name':'confirm_password',
        'id':'confirm_password',
        'autocomplete':'confirm_password',
        'placeholder':'Confirm password'
    }),label ='Confirm password')


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
     



class ChangeForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'username',
        'id':'login__username',
        'autocomplete':'username',
        'placeholder':'Username'
    }),label ='Username')
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'first_name',
        'id':'first_name',
        'autocomplete':'first_name',
        'placeholder':'First name'
    }),label ='First name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'last_name',
        'id':'last_name',
        'autocomplete':'last_name',
        'placeholder':'Last name'
    }),label ='Last name')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'email',
        'id':'email',
        'autocomplete':'email',
        'placeholder':'Email'
    }),label ='Email')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class LoginForm(forms.ModelForm):
   username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'text',
        'name':'username',
        'id':'login__username',
        'autocomplete':'username',
        'placeholder':'Username'
    }),label ='Username')
   password = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'password',
        'name':'password',
        'id':'password',
        'autocomplete':'password',
        'placeholder':'Password'
    }),label ='Password')
   class Meta:
        model = User
        fields = ['username', 'password']

class PassChangeForm(PasswordChangeForm):
   old_password = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'password',
        'name':'old_password',
        'id':'password',
        'autocomplete':'old_password',
        'placeholder':'Old password'
    }),label ='Old password')
   new_password = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'password',
        'name':'new_password',
        'id':'new_password',
        'autocomplete':'new_password',
        'placeholder':'New password'
    }),label ='New password')
   new_password_confirmation = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form__input',
        'type':'password',
        'name':'new_password_confirmation',
        'id':'new_password_confirmation',
        'autocomplete':'password',
        'placeholder':'New password confirmation'
    }),label ='New password confirmation')
   class Meta:
        model = User
        fields = ['old_password', 'new_password','new_password_confirmation']
