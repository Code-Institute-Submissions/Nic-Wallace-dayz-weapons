from django.test import TestCase
from django.contrib.auth.models import User
from .models import Weapon, Ammunition, Attachment, Category


class TestViews(TestCase):

    def setUp(self):
        Ammunition.objects.create(name='Test Ammunition')
        Attachment.objects.create(name='Test Attachment')
        Category.objects.create(name='Test Category')
        Weapon.objects.create(
            name='Test Weapon',
            ammunition=Ammunition(id=1),
            attachment=Attachment(id=1),
            category=Category(id=1)
        )
        self.user = User.objects.create_user(
            username='TestUser', password='Passw0rd', is_superuser=True)
        self.client.login(username='TestUser', password='Passw0rd')

    def test_get_weapons_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_add_weapon_page(self):
        page = self.client.get('/add/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'add_weapon.html')

    def test_get_edit_weapon_page(self):
        page = self.client.get('/edit_weapon/1/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'edit_weapon.html')
    
    def test_add_weapon(self):
        self.client.post(
            '/add/',
            {
                'name': 'Test Weapon',
                'description': 'Test description',
                'ammunition': 1,
                'attachment': 1,
                'category': 1,
                'size': 'Big',
                'weight': '1',
                'damage': 10,
                'image': 'placeholder',
                'is_public': 'False',
            }
        )
        weapon = Weapon.objects.filter(name='Test Weapon')[0]
        self.assertEqual('Test Weapon', weapon.name)

    def test_delete_weapon(self):
        weapon = Weapon.objects.filter(name='Test Weapon')[0]
        self.client.get(f'/delete_weapon/{weapon.id}', follow=True)
        weapon_delete = Weapon.objects.filter(name='Test Weapon').count()
        self.assertEqual(weapon_delete, 0)
