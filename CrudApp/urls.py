from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ItemCreateView.as_view(), name='item_create'),
    path('', views.ItemListView.as_view(), name='item_list'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='item_update'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='item_delete')
]
