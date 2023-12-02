from . import views
from django.urls import path


urlpatterns = [
    path('', views.WeaponList.as_view(), name='home'),
    path('<slug:slug>/', views.WeaponDetail.as_view(), name='weapon_detail'),
]
