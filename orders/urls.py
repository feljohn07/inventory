from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='orders'),
    path('add/', views.add_view, name='new_order'),
    path('add/save/', views.add),
    # add update
    # add delete
]