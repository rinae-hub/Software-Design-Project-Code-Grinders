from django.test import TestCase, Client
import unittest
from django.urls import reverse
from web.forms import UserRegisterForm, GenerateGraphForm
from web.models import student


class TestViews(TestCase):
    # creating a dummy data
    def setUp(self):
        self.student1=student.objects.create(StudentNumber = '70141',Gender='F',RegistrationStart='2008', RegistrationEnd='2018',Streamline='Biological Science Degree')
        self.student2=student.objects.create(StudentNumber = '70151',Gender='F',RegistrationStart='2013',RegistrationEnd='2012',Streamline='Biological Science Degree')
        self.student3=student.objects.create(StudentNumber = '714141',Gender='M',RegistrationStart='2015',RegistrationEnd='2011',Streamline='Biological Science Degree')
        self.student4=student.objects.create(StudentNumber = '79841',Gender='M',RegistrationStart='2016',RegistrationEnd='2016',Streamline='Biological Science Degree')
        self.student4=student.objects.create(StudentNumber = '728441',Gender='M',RegistrationStart='2018',RegistrationEnd='2008',Streamline='Biological Science Degree')
        self.student4=student.objects.create(StudentNumber = '788401',Gender='F',RegistrationStart='2018',RegistrationEnd='2015',Streamline='Biological Science Degree')
        self.student4=student.objects.create(StudentNumber = '788141',Gender='F',RegistrationStart='2018',RegistrationEnd='2018',Streamline='Biological Science Degree')

    # checking whether the ajax_generate_graph is returning data correctly as it should
    def test_ajax_view_POST(self):
        client= Client()
        response = self.client.post(reverse('ajax'),
        data={'dependent_extra_values':'RegistrationStart','dependent_values':'RegistrationEnd','colours':'#0000FF','name_1':'label1','name_2':'label2','graph_type':'bar'},
        content_type='application/json',HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEquals(response.status_code,200)

    '''Testing value returned by database are valid'''
    #Filtered by RegistrationStart and Biological Science Degree#
    def test_Biological_Science_Degree_in_ajax(self):
        y2008 =student.objects.filter(RegistrationStart='2008').filter(Streamline='Biological Science Degree').count()
        y2009 =student.objects.filter(RegistrationStart='2009').filter(Streamline='Biological Science Degree').count()
        y2010 =student.objects.filter(RegistrationStart='2010').filter(Streamline='Biological Science Degree').count()
        y2011 =student.objects.filter(RegistrationStart='2011').filter(Streamline='Biological Science Degree').count()
        y2012 =student.objects.filter(RegistrationStart='2012').filter(Streamline='Biological Science Degree').count()
        y2013 =student.objects.filter(RegistrationStart='2013').filter(Streamline='Biological Science Degree').count()
        y2014 =student.objects.filter(RegistrationStart='2014').filter(Streamline='Biological Science Degree').count()
        y2015 =student.objects.filter(RegistrationStart='2015').filter(Streamline='Biological Science Degree').count()
        y2016 =student.objects.filter(RegistrationStart='2016').filter(Streamline='Biological Science Degree').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Streamline='Biological Science Degree').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Streamline='Biological Science Degree').count()

        self.assertEquals(y2008,1)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,1)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,1)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,3)

    #Filtered by RegistrationEnd and Female#
    def test_deregistered_females_in_ajax(self):
        y2008 = student.objects.filter(RegistrationEnd='2008').filter(Gender='F').count()
        y2009 = student.objects.filter(RegistrationEnd='2009').filter(Gender='F').count()
        y2010 = student.objects.filter(RegistrationEnd='2010').filter(Gender='F').count()
        y2011 = student.objects.filter(RegistrationEnd='2011').filter(Gender='F').count()
        y2012 = student.objects.filter(RegistrationEnd='2012').filter(Gender='F').count()
        y2013 = student.objects.filter(RegistrationEnd='2013').filter(Gender='F').count()
        y2014 = student.objects.filter(RegistrationEnd='2014').filter(Gender='F').count()
        y2015 = student.objects.filter(RegistrationEnd='2015').filter(Gender='F').count()
        y2016 = student.objects.filter(RegistrationEnd='2016').filter(Gender='F').count()
        y2017 = student.objects.filter(RegistrationEnd='2017').filter(Gender='F').count()
        y2018 = student.objects.filter(RegistrationEnd='2018').filter(Gender='F').count()

        self.assertEquals(y2008,0)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,1)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,2)


    #Filtered by RegistrationEnd and males#
    def test_deregistered_males_in_ajax(self):
        y2008 = student.objects.filter(RegistrationEnd='2008').filter(Gender='M').count()
        y2009 = student.objects.filter(RegistrationEnd='2009').filter(Gender='M').count()
        y2010 = student.objects.filter(RegistrationEnd='2010').filter(Gender='M').count()
        y2011 = student.objects.filter(RegistrationEnd='2011').filter(Gender='M').count()
        y2012 = student.objects.filter(RegistrationEnd='2012').filter(Gender='M').count()
        y2013 = student.objects.filter(RegistrationEnd='2013').filter(Gender='M').count()
        y2014 = student.objects.filter(RegistrationEnd='2014').filter(Gender='M').count()
        y2015 = student.objects.filter(RegistrationEnd='2015').filter(Gender='M').count()
        y2016 = student.objects.filter(RegistrationEnd='2016').filter(Gender='M').count()
        y2017 = student.objects.filter(RegistrationEnd='2017').filter(Gender='M').count()
        y2018 = student.objects.filter(RegistrationEnd='2018').filter(Gender='M').count()

        self.assertEquals(y2008,1)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,1)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,0)
        self.assertEquals(y2016,1)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,0)

    #Filtered by RegistrationStart and females#
    def test_registered_females_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').filter(Gender='F').count()
        y2009 = student.objects.filter(RegistrationStart='2009').filter(Gender='F').count()
        y2010 = student.objects.filter(RegistrationStart='2010').filter(Gender='F').count()
        y2011 = student.objects.filter(RegistrationStart='2011').filter(Gender='F').count()
        y2012 = student.objects.filter(RegistrationStart='2012').filter(Gender='F').count()
        y2013 = student.objects.filter(RegistrationStart='2013').filter(Gender='F').count()
        y2014 = student.objects.filter(RegistrationStart='2014').filter(Gender='F').count()
        y2015 = student.objects.filter(RegistrationStart='2015').filter(Gender='F').count()
        y2016 = student.objects.filter(RegistrationStart='2016').filter(Gender='F').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Gender='F').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Gender='F').count()

        self.assertEquals(y2008,1)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,1)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,0)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,2)

    #Filtered by RegistrationStart and males#
    def test_registered_males_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').filter(Gender='M').count()
        y2009 = student.objects.filter(RegistrationStart='2009').filter(Gender='M').count()
        y2010 = student.objects.filter(RegistrationStart='2010').filter(Gender='M').count()
        y2011 = student.objects.filter(RegistrationStart='2011').filter(Gender='M').count()
        y2012 = student.objects.filter(RegistrationStart='2012').filter(Gender='M').count()
        y2013 = student.objects.filter(RegistrationStart='2013').filter(Gender='M').count()
        y2014 = student.objects.filter(RegistrationStart='2014').filter(Gender='M').count()
        y2015 = student.objects.filter(RegistrationStart='2015').filter(Gender='M').count()
        y2016 = student.objects.filter(RegistrationStart='2016').filter(Gender='M').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Gender='M').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Gender='M').count()


        self.assertEquals(y2008,0)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,1)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,1)

        #Filtered by RegistrationStart#
    def test_registered_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').count()
        y2009 = student.objects.filter(RegistrationStart='2009').count()
        y2010 = student.objects.filter(RegistrationStart='2010').count()
        y2011 = student.objects.filter(RegistrationStart='2011').count()
        y2012 = student.objects.filter(RegistrationStart='2012').count()
        y2013 = student.objects.filter(RegistrationStart='2013').count()
        y2014 = student.objects.filter(RegistrationStart='2014').count()
        y2015 = student.objects.filter(RegistrationStart='2015').count()
        y2016 = student.objects.filter(RegistrationStart='2016').count()
        y2017 = student.objects.filter(RegistrationStart='2017').count()
        y2018 = student.objects.filter(RegistrationStart='2018').count()

        self.assertEquals(y2008,1)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,1)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,1)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,3)

    def test_graph_view_GET(self):
        client = Client()
        form = GenerateGraphForm()
        response = client.get(reverse('graph'), data={'independent_variable':'Years','dependent_variable':'Registered Students','dependent_variable_extra':'Registered Students','colours':'Blue','graph_type':'Bar-Graph'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'graph.html')

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
