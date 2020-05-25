from django.test import TestCase, Client
from django.urls import reverse
from web.forms import UserRegisterForm

class TestViews(TestCase):

    def test_home_view_GET(self):
        client= Client()
        response=client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')

    def test_abc_view_GET(self):
        client= Client()
        response=client.get(reverse('abc'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'abc.html')

    def test_register_view_GET(self):
        client= Client()
        response=client.get(reverse('register'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'register.html')
    
    def redirect_view(self):
        self.assertRedirects(response,
        reverse('home'),
        status_code=302,
        target_status_code=200,
        fetch_redirect_response=False
        )

    def test_register_view_POST(self):
        client=Client()
        form=UserRegisterForm()
        response=client.post(reverse('register'),data={
        'username':"TAS",
        'email':"readEveryday@indo.co.za",
        'password1':"postcorona",
        'password2':"postcorona"
        })
        self.assertRedirects(response,
        reverse('login'),
        status_code=302,
        target_status_code=200,
        fetch_redirect_response=False
        )

