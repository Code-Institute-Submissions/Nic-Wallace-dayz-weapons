from django.shortcuts import render
from django.views import generic
from .models import Weapon

class WeaponList(generic.ListView):
    model = Weapon
    queryset = Weapon.objects.filter(is_public=True).order_by('name')
    template_name = 'index.html'
    paginate_by = 20
