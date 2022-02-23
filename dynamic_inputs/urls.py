from django.urls import path

from dynamic_inputs import views

urlpatterns = [
    path('add/', views.dynamic_inputs, name='add'),
    path('list/', views.data_list, name='list'),
    path('concrete/<int:id>', views.concrete_data, name='concrete'),
]
