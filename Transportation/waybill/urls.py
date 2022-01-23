from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(
        views.WaybillList.as_view(), login_url='/'
    ), name='list_waybill'),
    path('<str:sender>/<int:pk>', login_required(
        views.create_waybill, login_url='/driver/login'
    ), name='create_waybill'),
    path('detail/<int:pk>/', login_required(
        views.WaybillDetail.as_view(), login_url='/driver/login'
    ), name='detail_waybill'),
]
