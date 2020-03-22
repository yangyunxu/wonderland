from django.test import TestCase, RequestFactory
from django.urls import reverse
from myaccount.models import UserProfile
from django.contrib.auth.models import User
from myaccount.views import myaccount
# Create your tests here.

# Only 'singup' and 'login' could be presented because these two pages do not need users to login
class WhetherPagesCouldOpen(TestCase):
    def test(self):
        r1 = self.client.get(reverse('myaccount:signup'))
        r2 = self.client.get(reverse('myaccount:login'))
        r3 = self.client.get(reverse('myaccount:restricted'))
        r4 = self.client.get(reverse('myaccount:logout'))
        r5 = self.client.get(reverse('myaccount:myaccount'))
        r6 = self.client.get(reverse('myaccount:changepwd'))
        self.assertEqual(r1.status_code, 200)
        self.assertEqual(r2.status_code, 200)
        self.assertEqual(r3.status_code, 302)
        self.assertEqual(r4.status_code, 302)
        self.assertEqual(r5.status_code, 302)
        self.assertEqual(r6.status_code, 302)

class LoginViewTest(TestCase):
    def test_login(self):
        user = User.objects.get_or_create(username='1', password='1')[0]
        profile = UserProfile.objects.get_or_create(user=user, logInDate='2019-03-03', personalURL='https://blog.csdn.net/Lockey23/article/details/80656527', picture='')
        response = self.client.post('/myaccount/login/', {'username': '1', 'password': '1'})
        self.assertEqual(response.status_code, 200)

