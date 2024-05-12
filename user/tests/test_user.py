from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from user.views import CustomerSignUpView
from django.contrib.auth import get_user_model


class CustomerSignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_request(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')

    def test_post_request_with_valid_data(self):
        User = get_user_model() 
        response = self.client.post(reverse('customer_sign_up'), {'username': 'testuser', 'password1': 'testpassword123', 'password2': 'testpassword123'})
        self.assertEqual(response.status_code, 200)  

    def test_post_request_with_invalid_data(self):
        response = self.client.post(reverse('customer_sign_up'), {}) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/customer_sign_up.html')