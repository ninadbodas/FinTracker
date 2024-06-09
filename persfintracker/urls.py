from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.transaction_list, name='transaction_list'),
    path('new/', views.new_transaction, name='new_transaction'),
    path('edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
]