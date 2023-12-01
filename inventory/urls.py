from . import views
from django.urls import path


urlpatterns = [
    path('', views.WeaponList.as_view(), name='home'),
]
