from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Weapon

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
