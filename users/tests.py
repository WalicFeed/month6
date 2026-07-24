from django.test import TestCase
from .models import CustomUser


class CustomUserTests(TestCase):
    def test_create_user_without_phone_number(self):
        user = CustomUser.objects.create_user(email='user@example.com', password='12345')

        self.assertEqual(user.email, 'user@example.com')
        self.assertFalse(user.is_active)
        self.assertEqual(user.phone_number, '')

    def test_create_superuser_requires_phone_number(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have phone_number.'):
            CustomUser.objects.create_superuser(email='admin@example.com', password='12345')

        user = CustomUser.objects.create_superuser(
            email='admin2@example.com',
            password='12345',
            phone_number='+79999999999'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)
