from django.urls import path
from . import views as vs

app_name = 'accounts'

urlpatterns = [
    path('', vs.home, name='home'),
    path('products/', vs.products, name='products'),
    path('customer/', vs.customer, name='customer'),
]
