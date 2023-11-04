from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'shop'

urlpatterns = [
    path('', views.catalog, name='product_list'),
    path('<int:pk>', views.catalog, name='product_list'),
    path(_('item/<int:pk>'), views.detail, name='product'),
]