from urllib import response

from django.contrib.messages.storage import session
from django.test import TestCase, Client
from StuffTracker.models import Stuff, MyUser

# Create your tests here.
"""
Write a system test using Client that makes sure that on a successful login the correct user's item list is displayed. Load the test database with records to support your test.
Write a system test using Client that makes sure on an unsuccessful login, the home page is redisplayed with a message. Load the test database with records to support your test.
Write a system test that shows that an item added to the list immediately shows up in the rendered response. Load the test database with records to support your test.
"""

class addItems(TestCase):


    def setUp(self):
        self.client = Client()

        self.user = MyUser.objects.create(name="one", password="one")
        Stuff(name="cat", owner=self.user).save()


    def test_something(self):
         session = self.client.session
         session['somekey'] = 'test'
         session.save()
    def test_add_item(self):
        session = self.client.session
        session['user'] = self.user.name
        session.save()


        response = self.client.post('/things/', {'stuff': 'dragonfruit'}, follow=True)


        self.assertEqual(response.status_code, 200)


        self.assertContains(response, 'dragonfruit')


        self.assertTrue(Stuff.objects.filter(name='dragonfruit', owner=self.user).exists())

    def test_add_blank_item(self):
        session = self.client.session
        session['name'] = self.user.name
        session.save()

        initial_count = Stuff.objects.filter(owner=self.user).count()

        response = self.client.post('/things/', {'stuff': ''}, follow=True)

        self.assertEqual(response.status_code, 200)
        final_count = Stuff.objects.filter(owner=self.user).count()
        self.assertEqual(initial_count, final_count)

