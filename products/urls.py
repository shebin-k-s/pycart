from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name='home'),
    path("products/",views.products_view,name='products'),
    path("product",views.product_detail_view,name='product_detail')
]
