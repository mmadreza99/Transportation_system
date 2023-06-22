from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView, ListView, DetailView, UpdateView

from .forms import NewUserCustomer, LoginUserCustomer, CreateConsignmentForm, CreateCustomMoreForm
from .models import Consignment, CustomerMore
from account.models import CustomerUser


class LoginOrRegister(TemplateView):
    template_name = 'customer/LoginOrRegister.html'


class RegisterView(FormView):
    form_class = NewUserCustomer
    template_name = 'customer/register.html'
    success_url = '/customer/'

    def form_valid(self, form):
        form.save()
        messages.info(self.request, f"Registration {form.cleaned_data['username']} successful.")
        login(self.request, form.cleaned_data['user'])
        messages.info(self.request, f"You are now logged in as {form.cleaned_data['username']}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.info(self.request, f"Unable login with provided credentials.")
        return super().form_invalid(form)


class LoginView(FormView):
    form_class = LoginUserCustomer
    template_name = 'customer/login.html'
    success_url = '/customer/'

    def form_valid(self, form):
        login(request=self.request, user=form.cleaned_data['user'])
        messages.info(self.request, f"You are now logged in as {self.request.user}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.info(self.request, f"Unable login with provided credentials.")
        return super().form_invalid(form)


def logout_view(request):
    user = request.user
    logout(request)
    messages.info(request, f"You are now logout in as {user}.")
    return redirect('home_customer')


class HomeCustomer(TemplateView):
    template_name = 'customer/home_customer.html'


class CreateCustomerMore(FormView):
    form_class = CreateCustomMoreForm
    template_name = 'customer/create_customer_more.html'
    success_url = '/customer/profile/'

    def form_valid(self, form):
        messages.info(self.request, "create Customer More")
        form.cleaned_data['user'] = self.request.user
        form.save()
        return super(CreateCustomerMore, self).form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Unable create Customer More")
        return super(CreateCustomerMore, self).form_invalid(form)


class ProfileView(UpdateView):
    model = CustomerUser
    template_name = 'customer/profile_customer.html'
    fields = ('username', 'Social_Security', 'avatar')
    success_url = '/customer/profile/'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['More'] = CustomerMore.objects.filter(user=self.request.user)
        context['consignment'] = Consignment.objects.filter(sender=self.request.user)
        return context

    def form_valid(self, form):
        messages.info(self.request, f'item is update')
        return super(ProfileView, self).form_valid(form)


class ConsignmentListView(ListView):
    model = Consignment
    template_name = 'customer/consignment_list.html'
    paginate_by = 5


class ConsignmentDetailView(DetailView):
    model = Consignment
    template_name = 'customer/detail_consignment.html'

    def get_context_data(self, **kwargs):
        context = super(ConsignmentDetailView, self).get_context_data(**kwargs)
        context['type_user'] = self.request.user.type
        return context


class CreateConsignmentView(FormView):
    form_class = CreateConsignmentForm
    template_name = 'customer/create_consignment.html'
    success_url = '/customer/consignment/'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        messages.info(self.request, f"create Consignment {form.cleaned_data['name']}")
        form.save()
        return super(CreateConsignmentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.info(self.request, "Unable create Consignment")
        return super(CreateConsignmentView, self).form_invalid(form)


class UpdateConsignmentView(UpdateView):
    model = Consignment
    template_name = 'customer/update_consignment.html'
    success_url = '/customer/profile'
    fields = ('name', 'weight', 'package_type', 'number', 'recipient_destination', 'recipient_name', 'recipient_number')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.info(self.request, f"Update Consignment {form.cleaned_data['name']}")
        form.save()
        return super(UpdateConsignmentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.info(self.request, f"Unable Update Consignment {form.cleaned_data['name']}")
        return super(UpdateConsignmentView, self).form_invalid(form.errors)


