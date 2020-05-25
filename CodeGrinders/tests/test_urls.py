from django.test import SimpleTestCase
from django.urls import reverse, resolve
from web.views import register_view,abc, home_view
import django.contrib.auth.views


class TestUrls(SimpleTestCase):
    # testing whether the url to home-view is working
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func,register_view)

    # testing whether the url to login-view is working
    #def test_login_url_is_resolved(self):
        #url = reverse('login')
        #self.assertEquals(resolve(url).func.view_class,django.contrib.auth.views.LoginView)


    #testing whether the url to logout-view is working
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class,django.contrib.auth.views.LogoutView)


        #testing whether the url to abc-view is working
    def test_abc_url_is_resolved(self):
        url = reverse('abc')
        self.assertEquals(resolve(url).func,abc)


    # testing whether the url to home-view is working
    def test_home_url_is_resolved(self):
         url = reverse('home')
         self.assertEquals(resolve(url).func,home_view)
