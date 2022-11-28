from django.urls import path

from .views import ItemListView, ItemDetailView, CreateCheckoutView


urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('buy/<pk>/', CreateCheckoutView.as_view(), name='buy-item')
]