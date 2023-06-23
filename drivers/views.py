from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView

from waybill.models import Waybill
from .models import DriverMore, Certificate, Truck, KartHoshmand
from account.models import DriverUser

from .forms import (
    NewUserDriver, LoginUserDriver, RegisterKartHoshmand,
    RegisterMoreForm, RegisterCertificate, RegisterTruck
)


class LoginOrRegister(TemplateView):
    template_name = 'drivers/login_or_register.html'


class RegisterView(FormView):
    form_class = NewUserDriver
    template_name = 'drivers/register.html'
    success_url = '/driver/'

    def form_valid(self, form):
        form.save()
        messages.info(self.request, f"Registration {form.cleaned_data['username']} successful.")
        login(self.request, form.cleaned_data['user'])
        messages.info(self.request, f"You are now logged in as {form.cleaned_data['username']}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        self.success_url = reverse_lazy('driver_register')
        messages.info(self.request, f"Unable register with provided credentials.")
        return super().form_invalid(form)


class LoginView(FormView):
    form_class = LoginUserDriver
    template_name = 'drivers/login.html'
    success_url = '/driver/'

    def form_valid(self, form):
        login(request=self.request, user=form.cleaned_data['user'])
        messages.info(self.request, 'login')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        self.success_url = reverse_lazy('driver_register')
        messages.info(self.request, f"Unable login with provided credentials.")
        return super().form_valid(form)


def logout_view(request):
    user = request.user
    logout(request)
    messages.info(request, f"You are now logout in as {user}.")
    return redirect('home_driver')


class HomeDriver(TemplateView):
    template_name = 'drivers/home_driver.html'


class RegisterMoreView(FormView):
    form_class = RegisterMoreForm
    template_name = 'drivers/register_more.html'

    def form_valid(self, form):
        form.cleaned_data['user'] = self.request.user
        form.save()
        return super(RegisterMoreView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home_driver')


class RegisterUpdateMoreView(UpdateView):
    model = DriverMore
    fields = ('place_of_birth', 'Date_of_birth', 'address')
    template_name = 'drivers/register_more.html'

    def get_object(self, queryset=None):
        return self.request.user.more

    def form_valid(self, form):
        print('touch', form.cleaned_data['place_of_birth'])
        return super(RegisterUpdateMoreView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home_driver')


class RegisterCertificateView(FormView):
    form_class = RegisterCertificate
    template_name = 'drivers/register_certificate.html'

    def form_valid(self, form):
        form.cleaned_data['user'] = self.request.user.more
        form.save()
        return super(RegisterCertificateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home_driver')


class RegisterUpdateCertificateView(UpdateView):
    model = Certificate
    fields = ('validity_date', 'image')
    template_name = 'drivers/register_certificate.html'

    def get_object(self, queryset=None):
        return self.request.user.more.certificate

    def get_success_url(self):
        return reverse_lazy('home_driver')


class RegisterTruckView(FormView):
    form_class = RegisterTruck
    template_name = 'drivers/register_truck.html'

    def form_valid(self, form):
        form.cleaned_data['user'] = self.request.user.D_user
        form.save()
        return super(RegisterTruckView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home_driver')


class RegisterUpdateTruckView(UpdateView):
    model = Truck
    fields = ('type', 'image')
    template_name = 'drivers/register_truck.html'

    def get_object(self, queryset=None):
        return self.request.user.more.truck

    def get_success_url(self):
        return reverse_lazy('home_driver')


class RegisterKartView(FormView):
    form_class = RegisterKartHoshmand
    template_name = 'drivers/register_kart.html'

    def form_valid(self, form):
        form.cleaned_data['user'] = self.request.user.more
        form.save()
        return super(RegisterKartView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home_driver')


class RegisterUpdateKartView(UpdateView):
    model = KartHoshmand
    fields = ('validity_date', 'image')
    template_name = 'drivers/register_kart.html'

    def get_object(self, queryset=None):
        return self.request.user.more.kartHoshmand

    def get_success_url(self):
        return reverse_lazy('home_driver')


class ProfileView(UpdateView):
    model = DriverUser
    template_name = 'drivers/profile_driver.html'
    fields = ('username', 'Social_Security', 'avatar')

    def get_success_url(self):
        return reverse_lazy('home_driver')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        try:
            driver_user = self.request.user.more
        except:
            driver_user = None
        if driver_user:
            context['truck'] = Truck.objects.filter(user=driver_user).first()
            context['certificate'] = Certificate.objects.filter(user=driver_user).first()
            context['kart'] = KartHoshmand.objects.filter(user=driver_user).first()
            context['waybills'] = driver_user.waybill_driver.all().order_by('-created_on')
        return context

    def form_valid(self, form):
        messages.info(self.request, f'item is update')
        return super(ProfileView, self).form_valid(form)
