from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.catalog, name='product_list'),
    path('<pk>', views.catalog, name='product_list'),
    path('item/<pk>', views.detail, name='product'),
]