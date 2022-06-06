from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='purchases'),
    path('add/', views.add_view, name='new_purchase'),
    path('add/save/', views.add),
]