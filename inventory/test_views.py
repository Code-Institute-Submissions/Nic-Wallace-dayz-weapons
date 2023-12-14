from django.test import TestCase
from .models import Weapon

# Create your tests here.
class TestViews(TestCase):

    # def test_get_weapons_list(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'index.html')
    
    # This is throwing errors, is it because of the base template being used?
    # "no templates used to render the response" and 301 moved permanently error
    # # same errors for edit tests
    def test_get_add_weapon_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_weapon.html')

    def test_get_edit_weapon_page(self):
        response = self.client.get('/edit/2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_weapon.html')
    
    def test_add_weapon(self):
        response = self.client.post('/add', {'name': 'Test Added Weapon'})
        self.assertRedirects(response, 'home')

    def test_delete_weapon(self):
        weapon = Weapon.objects.create(name='Test Weapon', ammunition_id='1', attachment_id='1', category_id='1')
        response = self.client.get(f'/delete/{weapon.id}')
        self.assertRedirects(response, 'home')
        existing_weapon = Weapon.objects.filter(id=item.id)
        self.assertEqual(len(existing_weapon), 0)
