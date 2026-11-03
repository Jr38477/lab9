from django.test import TestCase, Client
from StuffTracker.models import Stuff, MyUser

# Create your tests here.
"""
Write a system test using Client that makes sure that on a successful login the correct user's item list is displayed. Load the test database with records to support your test.
Write a system test using Client that makes sure on an unsuccessful login, the home page is redisplayed with a message. Load the test database with records to support your test.
Write a system test that shows that an item added to the list immediately shows up in the rendered response. Load the test database with records to support your test.
"""

class LoginFail(TestCase):
    monkey = None
    thingList = None

    def setUp(self):
        # completed
        self.monkey = Client()
        self.thingList = {"one": ["cat", "dog"], "two": ["cake"]}
        # fill test database
        for i in self.thingList.keys():
            temp = MyUser(name=i, password=i)
            temp.save()
            for j in self.thingList[i]:
                Stuff(name=j, owner=temp).save()
    def test_bad_password(self):

        response = self.monkey.post('/login/', {'name': 'one', 'password': 'two'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "bad password")

    def test_blank_password(self):
        response = self.monkey.post('/login/', {'name': 'admin', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "bad password")

    def test_bad_username(self):
        response = self.monkey.post('/login/', {'name': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "bad username")

    def test_bad_username_and_password(self):
        response = self.monkey.post('/login/', {'name': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "bad username and password")



    # test methods should confirm correct error message is displayed when a bad password is entered.
    # I had separate tests for no password, someone else's password


class AddItem(TestCase):
    pass
    # need to create database in setup
    # confirm that after an add item form is submitted, that the new item is in the database and appears in the response webpage
