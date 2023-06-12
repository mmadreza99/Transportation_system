from django import forms

from .models import Waybill


class CreateWaybill(forms.ModelForm):
    class Meta:
        model = Waybill
        fields = ('more',)
        widgets = {
            'created_on': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        waybill = super(CreateWaybill, self).save()
        waybill.track_code = Waybill.generate_track_code()
        if commit:
            waybill.save()
        return waybill
