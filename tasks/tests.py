from django.test import TestCase
from users.models import CustomUser
from statuses.models import Statuses
from tasks.models import Tasks


class TaskTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        CustomUser.objects.create_user(**self.credentials)

    def create_status(self):
        return Statuses.objects.create(name='in work')

    def create_user(self, name, password):
        return CustomUser.objects.create_user({'username': name,
                                               'password': password})

    def test_create_task(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        status = self.create_status()
        some_user = self.create_user('nik', 'pas')
        Tasks.objects.create(name='test task', creator=some_user,
                             executor=some_user, status=status)
        self.assertEqual(Tasks.objects.count(), 1)
