from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic, View
from .models import Weapon
from .forms import WeaponForm


class WeaponList(generic.ListView):
    model = Weapon
    queryset = Weapon.objects.filter(is_public=True).order_by('name')
    template_name = 'index.html'
    paginate_by = 20


def weapon_details(request, id):
    """
    Page to display full weapon specs.
    """
    weapon = get_object_or_404(Weapon, id=id)
    template = 'weapon_detail.html'
    context = {
        'weapon': weapon,
    }
    return render(request, template, context)


def add_weapon(request):
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weapon_detail')

    form = WeaponForm()
    context = {
        'form': form
    }
    return render(request, 'add_weapon.html', context)
