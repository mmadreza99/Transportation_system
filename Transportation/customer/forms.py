from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomerUser


class NewUserCustomer(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomerUser
        fields = ("username", "email", "phone_number", "password1", "password2", "avatar")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginUserCustomer(UserCreationForm):

    class Meta:
        model = CustomerUser
        fields = ("username", "password")

