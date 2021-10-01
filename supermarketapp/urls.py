from supermarketapp import views
from django.urls import path

urlpatterns=[
#path("supermarket/",views.supermarket,name='supermarket'),
path("supermarket_save/",views.supermarket_save,name='supermarket_save'),
path("showbill/<name>",views.showBill,name='showbill')
]
