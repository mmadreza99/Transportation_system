from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import AuthorUser


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = AuthorUser
        fields = ("username", "email", "phone_number", "password1", "password2", "avatar")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginUserForm(forms.ModelForm):

    class Meta:
        model = AuthorUser
        fields = ("username", "password")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
