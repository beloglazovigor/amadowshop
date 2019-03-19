from django import forms
from django.contrib.auth.forms import AuthenticationForm
from authapp.models import ShopUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'input100',
             'type': 'text',
             'name': 'username',
             'placeholder': 'First Name',
             }
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'input100',
             'type': 'password',
             'name': 'password',
             'placeholder': 'Password',
             }
        )


class ShopUserRegisterForm(UserCreationForm):
    send_mode = forms.BooleanField(required=False)
    class Meta:
        model = ShopUser
        fields = (
            'username',
            'last_name',
            'email',
            'password1',
            'password2',
            'send_mode',
        )

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'input100',
             'type': 'text',
             'name': 'username',
             'placeholder': 'First Name',
             }
        )
        self.fields['last_name'].widget.attrs.update(
            {'class': 'input100',
             'type': 'text',
             'name': 'last_name',
             'placeholder': 'Last Name',
             }
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'input100',
             'type': 'text',
             'name': 'email',
             'placeholder': 'Email',
             }
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'input100',
             'type': 'password',
             'name': 'password1',
             'placeholder': 'Password',
             }
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'input100',
             'type': 'password',
             'name': 'password2',
             'placeholder': 'Confirm Password',
             }
        )
        self.fields['send_mode'].widget.attrs.update(
            {'class': 'input-checkbox100',
             'id': 'ckb1',
             'type': 'checkbox',
             }
        )


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'input100',
             'type': 'text',
             'name': 'username',
             }
        )
        self.fields['first_name'].widget.attrs.update(
            {'class': 'input100',
             'type': 'text',
             'name': 'first_name',
             }
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'input100',
             'type': 'text',
             'name': 'email',
             }
        )
