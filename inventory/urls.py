from . import views
from django.urls import path


urlpatterns = [
    path('', views.WeaponList.as_view(), name='home'),
    path('add/', views.add_weapon, name='add_weapon'),
    path('weapon/<int:id>/', views.weapon_details, name='weapon_detail'),
    path('edit_weapon/<int:id>/', views.edit_weapon, name='edit_weapon'),
    path('delete_weapon/<int:id>/', views.delete_weapon, name='delete_weapon'),
]
