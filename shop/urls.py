from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.catalog, name='product_list'),
    path('<int:pk>', views.catalog, name='product_list'),
    path('item/<int:pk>', views.detail, name='product'),
]