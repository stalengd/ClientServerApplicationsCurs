from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path(_('add/<product_id>/'), views.cart_add, name='cart_add'),
    path(_('remove/<product_id>/'), views.cart_remove, name='cart_remove'),
]