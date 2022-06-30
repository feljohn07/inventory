from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='products'),
    path('view/<int:id>', views.view_product),
    path('add/', views.add_view, name='new_product'),
    path('add/save/', views.add),
    path('update/<int:id>', views.update_view, name='update_product'),
    path('update/save/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('search/', views.search, name='search'),
]