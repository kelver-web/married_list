from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from core.models import ContactMessage



class GuestRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # garante que password1 e password2 fiquem bonitos
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirme a senha'
        })


class GuestLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha'
        })
    )




class ContactForm(forms.ModelForm):
   class Meta:
         model = ContactMessage
         fields = ['name', 'email', 'subject', 'message']
         widgets = {
              'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome'
              }),
              'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu e-mail'
              }),
                'subject': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Assunto'
                }),
              'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Sua mensagem',
                'rows': 5
              }),
         }
