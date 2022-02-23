from django.urls import path

from dynamic_inputs import views

urlpatterns = [
    path('', views.data_list, name='list'),
    path('add/', views.dynamic_inputs, name='add'),
    path('<int:id>', views.concrete_data, name='concrete'),
]
