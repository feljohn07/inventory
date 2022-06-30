from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='customers'),
    path('add/', views.add_view, name='new_customer'),
    path('add/save/', views.add),
    path('update/<int:id>', views.update_view),
    path('update/save/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('search/', views.search_customer, name='search_customer'),

]