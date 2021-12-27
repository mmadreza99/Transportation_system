from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from .forms import NewUserCustomer, LoginUserCustomer
from account.models import CustomerUser


def login_or_register(request):
    return render(request, "customer/LoginOrRegister.html", context={})


def register(request):
    form = NewUserCustomer
    if request.method == "POST":
        form = NewUserCustomer(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Registration {user.username} successful.")
            return redirect("home_customer")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, template_name="customer/register.html", context={"form": form})


def login_page(request):
    form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home_customer")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, template_name="customer/login.html", context={"form": form})


@login_required(login_url="/customer/login_or_register/")
def home_customer(request):
    return HttpResponse("home customer")
