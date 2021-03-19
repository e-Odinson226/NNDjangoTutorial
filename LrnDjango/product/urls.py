from django.urls import path

from .views import (    product_single_view,
                        products_view,
                        product_create_view,
                        product_delete_view   )
                        
app_name = "product"
urlpatterns = [
    path('', products_view, name="products"),
    path('<int:id>/', product_single_view, name="pDetail"),
    path('create/', product_create_view, name="pCreate"),
    path('<int:id>/delete', product_delete_view, name="pDelete"),

]
