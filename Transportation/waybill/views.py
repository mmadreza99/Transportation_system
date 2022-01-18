from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import CreateWaybill
from .models import Waybill
from account.models import CustomerUser
from customer.models import Consignment


class WaybillList(ListView):
    model = Waybill
    template_name = 'waybill_list.html'

    def get_queryset(self):
        if self.request.user.type == 'DRIVER':
            return Waybill.objects.filter(driver=self.request.user)
        elif self.request.user.type == 'CUSTOMER':
            return Waybill.objects.filter(sender=self.request.user)


class WaybillDetail(DetailView):
    model = Waybill
    template_name = 'detail_waybill.html'
    context_object_name = 'waybill'

    def get_object(self, queryset=None):
        return self.request.user


def create_waybill(request, sender, pk):
    customer = get_object_or_404(CustomerUser, username=sender)
    consignment = get_object_or_404(Consignment, id=pk)
    form = CreateWaybill()
    if request.method == 'POST':
        form = CreateWaybill(request.POST)
        form.instance.driver = request.user
        form.instance.sender = customer
        form.instance.consignment = consignment
        if form.is_valid():
            form.save()
        return render(request, 'show_waybill.html', context={'form': form,
                                                             'customer': customer,
                                                             'consignment': consignment})
    return render(request, 'show_waybill.html', context={'form': form,
                                                         'customer': customer,
                                                         'consignment': consignment})

