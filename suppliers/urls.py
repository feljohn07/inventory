from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='suppliers'),
    path('add/', views.add_view, name='new_supplier'),
    path('add/save/', views.add),
    path('update/<int:id>', views.update_view),
    path('update/save/<int:id>', views.update),
    # Delete Path
]