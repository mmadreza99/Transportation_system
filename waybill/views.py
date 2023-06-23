from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponse

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

    def get_queryset(self):
        if self.request.user.type == 'DRIVER':
            return Waybill.objects.filter(driver=self.request.user, pk=self.kwargs['pk'])
        elif self.request.user.type == 'CUSTOMER':
            return Waybill.objects.filter(sender=self.request.user, pk=self.kwargs['pk'])


def create_waybill(request, sender, pk):
    customer = get_object_or_404(CustomerUser, username=sender)
    consignment = get_object_or_404(Consignment, id=pk)
    if request.user.type != 'DRIVER':
        return HttpResponse('just user Driver can be take waybill')
    form = CreateWaybill()
    if request.method == 'POST':
        form = CreateWaybill(request.POST)
        form.instance.driver = request.user.more
        form.instance.sender = customer.more
        form.instance.consignment = consignment
        if form.is_valid():
            waybill = form.save()
            messages.info(request, 'successful create Waybill')
            return redirect('detail_waybill', pk=waybill.pk)
        return render(request, 'create_waybill.html', context={'form': form,
                                                               'customer': customer,
                                                               'consignment': consignment})
    return render(request, 'create_waybill.html', context={'form': form,
                                                           'customer': customer,
                                                           'consignment': consignment})
