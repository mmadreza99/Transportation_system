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
    class Meta:
        model = Consignment
        fields = ('name', 'weight', 'package_type', 'number', 'origin_of_sending',
                  'recipient_destination', 'recipient_name', 'recipient_number')

    def clean(self):
        return self.cleaned_data

    def save(self, commit=True):
        username = self.cleaned_data['user']
        consignment = Consignment.objects.create(
            sender=CustomerUser.objects.get(username=username),
            name=self.cleaned_data['name'],
            weight=self.cleaned_data['weight'],
            package_type=self.cleaned_data['package_type'],
            number=self.cleaned_data['number'],
            origin_of_sending=self.cleaned_data['origin_of_sending'],
            recipient_destination=self.cleaned_data['recipient_destination'],
            recipient_name=self.cleaned_data['recipient_name'],
            recipient_number=self.cleaned_data['recipient_number']
        )
        return super().save(consignment)


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
