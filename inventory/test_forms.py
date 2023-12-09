from django.test import TestCase
from .forms import WeaponForm

# Create your tests here.
class TestWeaponForm(TestCase):

    def test_weapon_name_is_required(self):
        form = WeaponForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_feilds_are_explicit_in_form_metacalss(self):
        form = WeaponForm()
        self.assertEqual(form.Meta.fields, [
            'name', 'description', 'ammunition', 'attachment',
            'category', 'size', 'weight', 'damage', 'image', 'is_public'
            ])
