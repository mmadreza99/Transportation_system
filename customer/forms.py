from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomerUser
from .models import Consignment, CustomerMore


User = get_user_model()


class NewUserCustomer(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomerUser
        fields = ("username", "email", "phone_number", "password1", "password2", "avatar")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'{username} already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'{email} already exists')
        return email

    def save(self, commit=True):
        user = super(NewUserCustomer, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.avatar = self.cleaned_data['avatar']
        if commit:
            user.save()
            self.cleaned_data['user'] = user
        return user


class LoginUserCustomer(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ("username", "password")

    def clean(self):
        username = self.cleaned_data['username']
        user = CustomerUser.objects.filter(username=username).first()
        if user is None:
            raise forms.ValidationError(f'{username} does not exists..')
        self.cleaned_data['user'] = user
        authentic = authenticate(**self.cleaned_data)
        if authentic is None:
            raise forms.ValidationError(f'Please enter the correct password.')
        return self.cleaned_data


class CreateConsignmentForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
    class Meta:
        model = Consignment
        field = '__all__'
        exclude = ('sender',)

    def clean(self):
        cleaned_data = super().clean()
        if self.user.type == "DRIVER":
            raise forms.ValidationError(f"this user can not create consignment")
        return cleaned_data


class CreateCustomMoreForm(forms.ModelForm):
    class Meta:
        model = CustomerMore
        fields = ('address', 'Postal_code')

    def save(self, commit=True):
        user = CustomerUser.objects.get(
            username=self.cleaned_data['user'])
        print(user)
        customer_more = CustomerMore.objects.create(
            user=user,
            address=self.cleaned_data['address'],
            Postal_code=self.cleaned_data['Postal_code']
        )
        return super().save(customer_more)
