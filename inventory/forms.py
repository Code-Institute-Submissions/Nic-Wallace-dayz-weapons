from django import forms
from .models import Weapon


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = [
            'name', 'description', 'ammunition', 'attachment',
            'category', 'size', 'weight', 'damage', 'image', 'is_public'
        ]
