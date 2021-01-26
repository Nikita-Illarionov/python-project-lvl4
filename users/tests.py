from django.test import TestCase, Client


class RegisterCase(TestCase):

    def test_register(self):
        c = Client()
        response = c.post('/users/create/', {'first_name': 'test',
                                             'last_name': 'test',
                                             'username': 'test',
                                             'password1': 'test',
                                             'password2': 'test'})
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        c = Client()
        c.post('/users/create/', {'first_name': 'test',
                                  'last_name': 'test',
                                  'username': 'test',
                                  'password1': 'test',
                                  'password2': 'test'})
        response = c.post('/login/', {'username': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 302)
