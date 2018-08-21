from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

User = get_user_model()


class UserRegistroForm(UserCreationForm):
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
                    'required': True})      
        }
