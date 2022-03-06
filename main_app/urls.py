from operator import ne
from django.urls import path
from main_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home),
    path('add/', views.add, name='add'),
    # Here, 'id' is an argument which is an integer type because 'int' refers to an integer data type.
    path('edit/<int:id>', views.edit, name='edit'),
    # Here, 'id' is an argument which is an integer type because 'int' refers to an integer data type.
    path('delete/<int:id>', views.delete, name='delete')
]
