from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='purchases'),
    path('add/', views.add_view, name='new_purchase'),
    path('add/save/', views.add),
    path('delete/<int:id>', views.delete),
    path('edit-quantity/', views.save_edit_quantity, name='update_purchase_quantity'),
]