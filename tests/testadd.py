from django.test import TestCase, Client
from StuffTracker.models import Stuff, MyUser


class addItems(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = MyUser.objects.create(name="one", password="one")
        Stuff.objects.create(name="cat", owner=self.user)

    def test_something(self):
        session = self.client.session
        session['somekey'] = 'test'
        session.save()

    def test_add_item(self):
        session = self.client.session
        session['name'] = self.user.name
        session.save()

        response = self.client.post('/things/', {'stuff': 'dragonfruit'}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'dragonfruit')
        self.assertTrue(
            Stuff.objects.filter(name='dragonfruit', owner=self.user).exists()
        )

    def test_add_blank_item(self):
        session = self.client.session
        session['name'] = self.user.name
        session.save()

        initial_count = Stuff.objects.filter(owner=self.user).count()

        response = self.client.post('/things/', {'stuff': ''}, follow=True)

        self.assertEqual(response.status_code, 200)
        final_count = Stuff.objects.filter(owner=self.user).count()
        self.assertEqual(initial_count, final_count)