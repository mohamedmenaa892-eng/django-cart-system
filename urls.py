from django.urls import path 
from . import views

urlpatterns = [
    path('',views.view_cart,name='cart'),
    path('add/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<int:cartitem_id>',views.remove_cartitem,name='remove_cartitem'),
    path('increase_item/<int:cartitem_id>',views.increase_item,name='increase_item'),
    path('decrease_item/<int:cartitem_id>',views.decrease_item,name='decrease_item'),
]