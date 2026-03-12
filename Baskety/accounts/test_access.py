from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AccessControlTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', password='password', role='admin')
        self.manager_user = User.objects.create_user(username='manager', password='password', role='manager')
        self.cashier_user = User.objects.create_user(username='cashier', password='password', role='cashier')
        self.client = Client()

    def test_admin_access(self):
        self.client.login(username='admin', password='password')
        urls = [
            reverse('inventory:dashboard'),
            reverse('reports:index'),
            reverse('pos:index'),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"Admin should access {url}")

    def test_manager_access(self):
        self.client.login(username='manager', password='password')
        urls = [
            reverse('inventory:dashboard'),
            reverse('reports:index'),
            reverse('pos:index'),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"Manager should access {url}")

    def test_cashier_access(self):
        self.client.login(username='cashier', password='password')
        
        # Should access POS
        response = self.client.get(reverse('pos:index'))
        self.assertEqual(response.status_code, 200, "Cashier should access POS")

        # Should NOT access Inventory
        response = self.client.get(reverse('inventory:dashboard'))
        self.assertEqual(response.status_code, 403, "Cashier should be denied access to Inventory")

        # Should NOT access Reports
        response = self.client.get(reverse('reports:index'))
        self.assertEqual(response.status_code, 403, "Cashier should be denied access to Reports")
