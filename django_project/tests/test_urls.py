from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import register_view
from pages.views import home_view, log_view, base_view, team_view, mentors_view
import django.contrib.auth.views


class TestUrls(SimpleTestCase):


    '''Tests for authentication'''
    # testing whether the url to login-view is working
    def test_login_url_is_resolved(self):
        url = reverse('login1')
        self.assertEquals(resolve(url).func.view_class,django.contrib.auth.views.LoginView)

    #testing whether the url to logout-view is working
    def test_logout_url_is_resolved(self):
        url = reverse('logout1')
        self.assertEquals(resolve(url).func.view_class,django.contrib.auth.views.LogoutView)

    #testing whether the url to register-view is working
    def test_register_url_is_resolved(self):
        url = reverse('register1')
        self.assertEquals(resolve(url).func,register_view)



    '''Tests for page urls'''
   # testing whether the url to home-view is working
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func,home_view)

   # testing whether the url to log-view is working
    def test_log_url_is_resolved(self):
        url = reverse('log')
        self.assertEquals(resolve(url).func,log_view)

   # testing whether the url to base-view is working
    def test_base_url_is_resolved(self):
        url = reverse('base')
        self.assertEquals(resolve(url).func,base_view)

    # testing whether the url to team-view is working
    def test_team_url_is_resolved(self):
        url = reverse('team')
        self.assertEquals(resolve(url).func,team_view)

   # testing whether the url to mentors-view is working
    def test_mentors_url_is_resolved(self):
        url = reverse('mentors')
        self.assertEquals(resolve(url).func,mentors_view)
