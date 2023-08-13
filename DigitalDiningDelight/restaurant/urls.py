# restaurant/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu-list'),
    path('place-order/', views.place_order, name='place-order'),
    path('admin/', views.admin_page, name='admin-page'),
]
