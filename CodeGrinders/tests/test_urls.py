from django.test import SimpleTestCase
from django.urls import reverse, resolve
from web.views import register_view,abc, home_view
import django.contrib.auth.views

#urlpatterns = [
#   path('abc/', views.abc, name='abc'), tested
#    path('graph/', views.graph, name='graph'),tested
#    path('',views.home_view, name='home'), tested
#    path('home/', views.redirect_view), 
#    path('ajax/', views.ajax_generate_graph, name='ajax'), tested
#    path('register/', views.register_view, name='register')tested
#]


class TestUrls(SimpleTestCase):
    # testing whether the url to home-view is working
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func,register_view)

    # testing whether the url to login-view is working
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class,django.contrib.auth.views.LoginView)
    
        
    def test_graph_url_is_resolved(self):
        url = reverse('graph')
        self.assertEquals(resolve(url).func,graph)


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
