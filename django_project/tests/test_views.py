from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

    def test_home_view_GET(self):
        client= Client()
        response=client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')

    def test_log_view_GET(self):
        client= Client()
        response=client.get(reverse('log'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'log.html')

    def test_base_view_GET(self):
        client= Client()
        response=client.get(reverse('base'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'base.html')

    def test_team_view_GET(self):
        client= Client()
        response=client.get(reverse('team'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'team.html')

    def test_mentors_view_GET(self):
        client= Client()
        response=client.get(reverse('mentors'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'mentors.html')

    def test_register_view_GET(self):
        client= Client()
        response=client.get(reverse('register1'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'accounts/register1.html')


    def test_register_view_GET(self):
        client= Client()
        response=client.get(reverse('register1'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'accounts/register1.html')

    ## post test_register_view still missing
