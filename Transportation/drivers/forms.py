from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import User, DriverUser
from .models import DriverMore, Certificate, Truck, KartHoshmand


class NewUserDriver(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = DriverUser
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
        user = super(NewUserDriver, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.avatar = self.cleaned_data['avatar']
        if commit:
            user.save()
            self.cleaned_data['user'] = user
        return user


class LoginUserDriver(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = DriverUser
        fields = ("username", "password")

    def clean(self):
        username = self.cleaned_data['username']
        user = DriverUser.objects.filter(username=username).first()
        if user is None:
            print(f'{username} does not exists..')
            raise forms.ValidationError(f'{username} does not exists..')
        self.cleaned_data['user'] = user
        authentic = authenticate(**self.cleaned_data)
        if authentic is None:
            print('Please enter the correct password.')
            raise forms.ValidationError(f'Please enter the correct password.')
        return self.cleaned_data


class RegisterMoreForm(forms.ModelForm):
    class Meta:
        model = DriverMore
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'Date_of_birth': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        more = super(RegisterMoreForm, self).save(commit=False)
        more.user = self.cleaned_data['user']
        if commit:
            more.save()
        return more


class RegisterCertificate(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'created_time': forms.widgets.DateInput(attrs={'type': 'date'}),
            'validity_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        certificate = super(RegisterCertificate, self).save(commit=False)
        certificate.user = self.cleaned_data['user']
        if commit:
            certificate.save()
        return certificate


class RegisterTruck(forms.ModelForm):
    class Meta:
        model = Truck
        fields = '__all__'
        exclude = ['user']

    def save(self, commit=True):
        truck = super(RegisterTruck, self).save(commit=False)
        truck.user = self.cleaned_data['user']
        if commit:
            truck.save()
        return truck


class RegisterKartHoshmand(forms.ModelForm):
    class Meta:
        model = KartHoshmand
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'create_time': forms.widgets.DateInput(attrs={'type': 'date'}),
            'validity_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        kart = super(RegisterKartHoshmand, self).save(commit=False)
        kart.user = self.cleaned_data['user']
        if commit:
            kart.save()
        return kart
