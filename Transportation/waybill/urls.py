from django.urls import path

from . import views

urlpatterns = [
    path('', views.WaybillList.as_view(), name='list_waybill'),
    path('<str:sender>/<int:pk>', views.create_waybill, name='create_waybill'),
    path('detail/<int:pk>/', views.WaybillDetail.as_view(), name='detail_waybill'),
]
