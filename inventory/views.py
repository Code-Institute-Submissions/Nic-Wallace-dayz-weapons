from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Weapon
from .forms import WeaponForm

class WeaponList(generic.ListView):
    model = Weapon
    queryset = Weapon.objects.filter(is_public=True).order_by('name')
    template_name = 'index.html'
    paginate_by = 20


class WeaponDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Weapon.objects.filter(is_public=True)
        weapon = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "weapon_detail.html",
            {"weapon": weapon,}
        )


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
