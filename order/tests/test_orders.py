import pdb
from django.test import TestCase, override_settings
from django.conf import settings
from django.urls import reverse
from user.models import User

class OrderTestCase(TestCase):   
    def setUp(self):
        products = '125496'
        self.user = User.objects.create_user(username='testuser', password='12345', old_cart=products)
        # self.order = Order.objects.create(
        #     order_id=1,
        #     date_created=timezone.now(),
        #     customer=self.user,
        #     status='Pending'
        # )

    @override_settings(ROOT_URLCONF='order.urls')
    def test_generate_pdf(self): 
        # pdb.set_trace()
        self.client.login(username='testuser', password='12345') 
        response = self.client.get(reverse('order_create'))
        
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        expected_filename = f'order_{self.order.order_id}.pdf'
        self.assertIn(expected_filename, response['Content-Disposition'])
