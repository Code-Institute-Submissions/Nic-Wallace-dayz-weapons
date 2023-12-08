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
    """
    Form for superuser/admin to add weapons.
    """
    # check if user is superuser; redirect if not
    if not request.user.is_superuser:
        messages.error(request, "Access Denied! Only admins can perform that action.")
        return redirect('home')
    # is a superuser; can proceed
    if request.method == 'POST':
        form = WeaponForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Weapon successfully added!')
            return redirect('home')
    form = WeaponForm()
    template = 'add_weapon.html'
    context = {
        'form': form
    }
    return render(request, template, context)

