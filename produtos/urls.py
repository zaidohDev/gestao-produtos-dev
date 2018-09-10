
from django.urls import path
from produtos.views import products_list, products_new, products_update, products_delete


urlpatterns = [
    path('list/', products_list, name='products_list'),
    path('new/', products_new, name='products_new'),
    path('update/<int:id>/', products_update, name='products_update'),
    path('delete/<int:id>/', products_delete, name='products_delete')
]