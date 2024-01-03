from django.contrib.auth import forms as auth_forms
from petstagram.accounts.models import PetstagramUser
from django import forms


class PetstagramUserCreateForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = PetstagramUser
        fields = ('username', 'email')


class LoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={'autofocus': True, 'placeholder': 'Username'}
        ),
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'placeholder': 'Password'},
        ),
    )


class PetstagramUserEditForm(forms.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'first_name': "First Name:",
            'last_name': "Last Name:",
            'email': 'Email:',
            'profile_picture': 'Image:',
            'gender': 'Gender:'
        }
