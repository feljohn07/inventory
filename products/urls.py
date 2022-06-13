from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='products'),
    path('add/', views.add_view, name='new_product'),
    path('add/save/', views.add),
    path('update/<int:id>', views.update_view, name='update_product'),
    path('update/save/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]