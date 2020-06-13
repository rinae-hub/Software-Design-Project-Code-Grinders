from django.test import TestCase, Client
from django.urls import reverse
from web.forms import UserRegisterForm

class TestViews(TestCase):

    def test_ajax_view_POST(self):
        dependent_values =[1043, 514, 538, 568, 553, 622, 621, 709, 783, 715, 796]
        dependent_values_1 =[1043, 514, 538, 568, 553, 622, 621, 709, 783, 715, 796]
        bar = 'bar'
        color = '#0000FF'
        label1 ='label1'
        label2 ='label2'
        client= Client()
        response = self.client.post(
        reverse('ajax'),
        data={'dependent_extra_values':dependent_values_1,'dependent_values':dependent_values,'colours':color,'name_1':label1,'name_2':label2,'graph_type':bar},
        content_type='application/json',
        HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEquals(response.status_code,200)



    # testing home view
    def test_home_view_GET(self):
        client= Client()
        response=client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')

    # testing abc view
    def test_abc_view_GET(self):
        client= Client()
        response=client.get(reverse('abc'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'abc.html')

    # testing register view method.GET
    def test_register_view_GET(self):
        client= Client()
        response=client.get(reverse('register'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'register.html')

    # testing register view method.POST
    def test_register_view_POST(self):
        client=Client()
        form=UserRegisterForm()
        response=client.post(reverse('register'),data={'username':"TAS",'email':"readEveryday@indo.co.za",'password1':"postcorona",'password2':"postcorona"})
        self.assertRedirects(response,reverse('login'),status_code=302,target_status_code=200,fetch_redirect_response=False)
