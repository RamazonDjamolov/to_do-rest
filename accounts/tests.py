# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from accounts.models import User
from accounts.serializers import UserCreateSerializer
from rest_framework.exceptions import ErrorDetail
from rest_framework.reverse import reverse

user = get_user_model()


# UnitTests
class UserCreateSerializersIsValidTests(TestCase):
    def setUp(self):
        self.validate_data = {
            'email': 'test0@gmail.com',
            'username': 'test0',
            'password': 'test',
            're_password': 'test'
        }

        self.not_validate_data = {
            'email': 'test0',
            'username': 'test0',
            'password': 'test1',
            're_password': 'test2'
        }

    def test_user_serializers_is_valid(self):
        serializers = UserCreateSerializer(data=self.validate_data)
        self.assertTrue(serializers.is_valid())
        self.assertEqual(serializers.errors, {})

    def test_user_serializer_is_isvalid(self):
        serializers = UserCreateSerializer(data=self.not_validate_data)
        self.assertFalse(serializers.is_valid())
        # print(serializers.errors, "my erors")
        self.assertEqual(serializers.errors,
                         {'email': [ErrorDetail(string='Enter a valid email address.', code='invalid')]})


class UserRegisterSerializersTests(TestCase):
    def setUp(self):
        self.register_data = {
            'email': 'test0@gmail.com',
            'username': 'test0',
            'password': 'test',
            're_password': 'test'
        }
        self.client = Client()
        self.register_url = reverse('register')

    def test_user_register_serializers(self):
        response = self.client.post(
            self.register_url,
            data=self.register_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'test')


class LoginSerializersTests(TestCase):
    def setUp(self):
        self.data = {
            "email": "admin@gmail.com",
            'username': 'admin',
            "password": "12"

        }
        user = User.objects.create_user(email=self.data['email'], username=self.data['username'],
                                        password=self.data['password'])

        self.login_data = {
            "email": "admin@gmail.com",
            "password": "12"
        }

        self.client = Client()
        self.login_url = reverse('token_obtain_pair')

    def test_login_serializers(self):
        response = self.client.post(
            self.login_url,
            data=self.login_data
        )
        print(response.data)

        self.assertEqual(response.status_code, 200)


