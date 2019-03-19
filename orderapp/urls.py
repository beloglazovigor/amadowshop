from django.urls import path
import orderapp.views as orderapp

app_name = 'orderapp'

urlpatterns = [
    path('orders-list', orderapp.OrderList.as_view(), name='orders_list'),
    path('forming/complete/<int:pk>/',
         orderapp.order_forming_complete, name='order_forming_complete'),
    path('create/', orderapp.OrderItemsCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', orderapp.OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', orderapp.OrderItemsUpdate.as_view(),
         name='order_update'),
    path('delete/<int:pk>/', orderapp.OrderDelete.as_view(),
         name='order_delete'),
]
