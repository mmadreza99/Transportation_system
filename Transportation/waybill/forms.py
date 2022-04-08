from django import forms

from .models import Waybill


class CreateWaybill(forms.ModelForm):
    class Meta:
        model = Waybill
        fields = ('more',)

    def save(self, commit=True):
        waybill = super(CreateWaybill, self).save()
        if commit:
            waybill.save()
        return waybill
