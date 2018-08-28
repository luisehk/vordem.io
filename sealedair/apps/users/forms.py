from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput
from .models import Profile
from betterforms.multiform import MultiModelForm

User = get_user_model()


class UserRegistroForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': "Nombre(s)",
            'last_name': "Apellidos",
            'email': "Email",
        }
        widgets = {
            'first_name': TextInput(
                attrs={
                    'required': True}),
            'last_name': TextInput(
                attrs={
                    'required': True}),
            'email': TextInput(
                attrs={
                    'type': 'email',
                    'required': True})
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        labels = {
            'first_name': "Nombre(s)",
            'last_name': "Apellidos",
        }
        widgets = {
            'first_name': TextInput(
                attrs={
                    'required': True}),
            'last_name': TextInput(
                attrs={
                    'required': True})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)


class UserProfileForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'profile': ProfileForm,
    }
