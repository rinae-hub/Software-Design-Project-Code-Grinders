from django.test import TestCase, Client
import unittest
from django.urls import reverse
from web.forms import UserRegisterForm, GenerateGraphForm
from web.models import student
import json


class TestViews(TestCase):
    # creating a dummy data
    def setUp(self):
        self.student1=student.objects.create(StudentNumber = '70141',Gender='F',YearStarted='2016',RegistrationStart='2008',Qualified='Q',RegistrationEnd='2018',Streamline='Biological Science Degree')
        self.student2=student.objects.create(StudentNumber = '70151',Gender='F',YearStarted='2009',RegistrationStart='2013',Qualified='Q',RegistrationEnd='2012',Streamline='Mathematics Degree')
        self.student3=student.objects.create(StudentNumber = '714141',Gender='M',YearStarted='2011',RegistrationStart='2015',Qualified='F',RegistrationEnd='2011',Streamline='Physical Science Degree')
        self.student5=student.objects.create(StudentNumber = '79841',Gender='M',YearStarted='2017',RegistrationStart='2016',Qualified='F',RegistrationEnd='2016',Streamline='Mathematics Degree')
        self.student6=student.objects.create(StudentNumber = '728441',Gender='M',YearStarted='2016',RegistrationStart='2018',Qualified='F',RegistrationEnd='2008',Streamline='Biological Science Degree')
        self.student7=student.objects.create(StudentNumber = '788401',Gender='F',YearStarted='2011',RegistrationStart='2018',Qualified='Q',RegistrationEnd='2015',Streamline='Mathematics Degree')
        self.student8=student.objects.create(StudentNumber = '788141',Gender='F',YearStarted='2013',RegistrationStart='2018',Qualified='Q',RegistrationEnd='2018',Streamline='Biological Science Degree')
        self.student9=student.objects.create(StudentNumber = '6521',Gender='F',YearStarted='2016',RegistrationStart='2008', Qualified='Q',RegistrationEnd='2018',Streamline='Mathematics Degree')
        self.student10=student.objects.create(StudentNumber = '54112',Gender='F',YearStarted='2009',RegistrationStart='2013',Qualified='F',RegistrationEnd='2012',Streamline='Physical Science Degree')
        self.student11=student.objects.create(StudentNumber = '4514',Gender='F',YearStarted='2011',RegistrationStart='2015',Qualified='Q',RegistrationEnd='2011',Streamline='Biological Science Degree')
        self.student12=student.objects.create(StudentNumber = '4471',Gender='M',YearStarted='2017',RegistrationStart='2016',Qualified='F',RegistrationEnd='2016',Streamline='Mathematics Degree')
        self.student13=student.objects.create(StudentNumber = '1127',Gender='M',YearStarted='2016',RegistrationStart='2018',Qualified='Q',RegistrationEnd='2008',Streamline='Physical Science Degree')
        self.student14=student.objects.create(StudentNumber = '00141',Gender='M',YearStarted='2011',RegistrationStart='2018',Qualified='F',RegistrationEnd='2015',Streamline='Biological Science Degree')
        self.student15=student.objects.create(StudentNumber = '895450',Gender='F',YearStarted='2013',RegistrationStart='2018',Qualified='Q',RegistrationEnd='2018',Streamline='Biological Science Degree')



    # checking whether the ajax_generate_graph is returning data correctly as it should
    def test_ajax_view_POST(self):
        client= Client()

        response = self.client.post(reverse('ajax'),
        json.dumps({
        "independent_variable": "years","dependent_variable":"RegistrationStart",
        "dependent_variable_extra": "Blank","colours": "#00FF00","graph_type": "bar",
        "csrfmiddlewaretoken": "c5uwGWhQV2xzWBfwPKO2PIqGd88DgyzLtKf56"
        }),
        content_type='json',HTTP_X_REQUESTED_WITH='XMLHttpRequest')
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
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,4)

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
        self.assertEquals(y2011,1)
        self.assertEquals(y2012,2)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,4)


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

        self.assertEquals(y2008,2)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,1)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,2)
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

        self.assertEquals(y2008,2)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,2)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,3)

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
        self.assertEquals(y2016,2)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,3)

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

        self.assertEquals(y2008,2)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,2)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,2)
        self.assertEquals(y2016,2)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,6)

        #Filtered by RegistrationEnd#
    def test_deregistered_in_ajax(self):
        y2008 = student.objects.filter(RegistrationEnd='2008').count()
        y2009 = student.objects.filter(RegistrationEnd='2009').count()
        y2010 = student.objects.filter(RegistrationEnd='2010').count()
        y2011 = student.objects.filter(RegistrationEnd='2011').count()
        y2012 = student.objects.filter(RegistrationEnd='2012').count()
        y2013 = student.objects.filter(RegistrationEnd='2013').count()
        y2014 = student.objects.filter(RegistrationEnd='2014').count()
        y2015 = student.objects.filter(RegistrationEnd='2015').count()
        y2016 = student.objects.filter(RegistrationEnd='2016').count()
        y2017 = student.objects.filter(RegistrationEnd='2017').count()
        y2018 = student.objects.filter(RegistrationEnd='2018').count()

        self.assertEquals(y2008,2)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,2)
        self.assertEquals(y2012,2)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,2)
        self.assertEquals(y2016,2)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,4)

        #Filtered by yearstarted#
    def test_yearstarted_in_ajax(self):
        y2008 = student.objects.filter(YearStarted='2008').count()
        y2009 = student.objects.filter(YearStarted='2009').count()
        y2010 = student.objects.filter(YearStarted='2010').count()
        y2011 = student.objects.filter(YearStarted='2011').count()
        y2012 = student.objects.filter(YearStarted='2012').count()
        y2013 = student.objects.filter(YearStarted='2013').count()
        y2014 = student.objects.filter(YearStarted='2014').count()
        y2015 = student.objects.filter(YearStarted='2015').count()
        y2016 = student.objects.filter(YearStarted='2016').count()
        y2017 = student.objects.filter(YearStarted='2017').count()
        y2018 = student.objects.filter(YearStarted='2018').count()

        self.assertEquals(y2008,0)
        self.assertEquals(y2009,2)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,4)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,2)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,0)
        self.assertEquals(y2016,4)
        self.assertEquals(y2017,2)
        self.assertEquals(y2018,0)

    #Filtered by Streamline= Mathematics Degree#
    def test_mathematics_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').filter(Streamline='Mathematics Degree').count()
        y2009 = student.objects.filter(RegistrationStart='2009').filter(Streamline='Mathematics Degree').count()
        y2010 = student.objects.filter(RegistrationStart='2010').filter(Streamline='Mathematics Degree').count()
        y2011 = student.objects.filter(RegistrationStart='2011').filter(Streamline='Mathematics Degree').count()
        y2012 = student.objects.filter(RegistrationStart='2012').filter(Streamline='Mathematics Degree').count()
        y2013 = student.objects.filter(RegistrationStart='2013').filter(Streamline='Mathematics Degree').count()
        y2014 = student.objects.filter(RegistrationStart='2014').filter(Streamline='Mathematics Degree').count()
        y2015 = student.objects.filter(RegistrationStart='2015').filter(Streamline='Mathematics Degree').count()
        y2016 = student.objects.filter(RegistrationStart='2016').filter(Streamline='Mathematics Degree').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Streamline='Mathematics Degree').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Streamline='Mathematics Degree').count()

        self.assertEquals(y2008,1)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,1)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,0)
        self.assertEquals(y2016,2)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,1)

        #Filtered by Streamline= Physical Science Degree#
    def test_physical_science_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').filter(Streamline='Physical Science Degree').count()
        y2009 = student.objects.filter(RegistrationStart='2009').filter(Streamline='Physical Science Degree').count()
        y2010 = student.objects.filter(RegistrationStart='2010').filter(Streamline='Physical Science Degree').count()
        y2011 = student.objects.filter(RegistrationStart='2011').filter(Streamline='Physical Science Degree').count()
        y2012 = student.objects.filter(RegistrationStart='2012').filter(Streamline='Physical Science Degree').count()
        y2013 = student.objects.filter(RegistrationStart='2013').filter(Streamline='Physical Science Degree').count()
        y2014 = student.objects.filter(RegistrationStart='2014').filter(Streamline='Physical Science Degree').count()
        y2015 = student.objects.filter(RegistrationStart='2015').filter(Streamline='Physical Science Degree').count()
        y2016 = student.objects.filter(RegistrationStart='2016').filter(Streamline='Physical Science Degree').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Streamline='Physical Science Degree').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Streamline='Physical Science Degree').count()

        self.assertEquals(y2008,0)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,1)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,1)


    #Filtered by Streamline= Earth Science Degree#
    def test_earth_science_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').filter(Streamline='Earth Science Degree').count()
        y2009 = student.objects.filter(RegistrationStart='2009').filter(Streamline='Earth Science Degree').count()
        y2010 = student.objects.filter(RegistrationStart='2010').filter(Streamline='Earth Science Degree').count()
        y2011 = student.objects.filter(RegistrationStart='2011').filter(Streamline='Earth Science Degree').count()
        y2012 = student.objects.filter(RegistrationStart='2012').filter(Streamline='Earth Science Degree').count()
        y2013 = student.objects.filter(RegistrationStart='2013').filter(Streamline='Earth Science Degree').count()
        y2014 = student.objects.filter(RegistrationStart='2014').filter(Streamline='Earth Science Degree').count()
        y2015 = student.objects.filter(RegistrationStart='2015').filter(Streamline='Earth Science Degree').count()
        y2016 = student.objects.filter(RegistrationStart='2016').filter(Streamline='Earth Science Degree').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Streamline='Earth Science Degree').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Streamline='Earth Science Degree').count()

        self.assertEquals(y2008,0)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,0)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,0)

    #Filtered by Unknown Streamline#
    def test_unknownstreamline_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').filter(Streamline='Unknown Streamline').count()
        y2009 = student.objects.filter(RegistrationStart='2009').filter(Streamline='Unknown Streamline').count()
        y2010 = student.objects.filter(RegistrationStart='2010').filter(Streamline='Unknown Streamline').count()
        y2011 = student.objects.filter(RegistrationStart='2011').filter(Streamline='Unknown Streamline').count()
        y2012 = student.objects.filter(RegistrationStart='2012').filter(Streamline='Unknown Streamline').count()
        y2013 = student.objects.filter(RegistrationStart='2013').filter(Streamline='Unknown Streamline').count()
        y2014 = student.objects.filter(RegistrationStart='2014').filter(Streamline='Unknown Streamline').count()
        y2015 = student.objects.filter(RegistrationStart='2015').filter(Streamline='Unknown Streamline').count()
        y2016 = student.objects.filter(RegistrationStart='2016').filter(Streamline='Unknown Streamline').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Streamline='Unknown Streamline').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Streamline='Unknown Streamline').count()

        self.assertEquals(y2008,0)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,0)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,0)

    #Filtered by RegistrationStart,Q,M#
    def test_qualified_males_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').filter(Qualified='Q').filter(Gender='M').count()
        y2009 = student.objects.filter(RegistrationStart='2009').filter(Qualified='Q').filter(Gender='M').count()
        y2010 = student.objects.filter(RegistrationStart='2010').filter(Qualified='Q').filter(Gender='M').count()
        y2011 = student.objects.filter(RegistrationStart='2011').filter(Qualified='Q').filter(Gender='M').count()
        y2012 = student.objects.filter(RegistrationStart='2012').filter(Qualified='Q').filter(Gender='M').count()
        y2013 = student.objects.filter(RegistrationStart='2013').filter(Qualified='Q').filter(Gender='M').count()
        y2014 = student.objects.filter(RegistrationStart='2014').filter(Qualified='Q').filter(Gender='M').count()
        y2015 = student.objects.filter(RegistrationStart='2015').filter(Qualified='Q').filter(Gender='M').count()
        y2016 = student.objects.filter(RegistrationStart='2016').filter(Qualified='Q').filter(Gender='M').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Qualified='Q').filter(Gender='M').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Qualified='Q').filter(Gender='M').count()


        self.assertEquals(y2008,0)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,0)
        self.assertEquals(y2016,0)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,1)

    #Filtered by RegistrationStart,F,M#
    def test_not_qualified_males_in_ajax(self):
        y2008 = student.objects.filter(RegistrationStart='2008').filter(Qualified='F').filter(Gender='M').count()
        y2009 = student.objects.filter(RegistrationStart='2009').filter(Qualified='F').filter(Gender='M').count()
        y2010 = student.objects.filter(RegistrationStart='2010').filter(Qualified='F').filter(Gender='M').count()
        y2011 = student.objects.filter(RegistrationStart='2011').filter(Qualified='F').filter(Gender='M').count()
        y2012 = student.objects.filter(RegistrationStart='2012').filter(Qualified='F').filter(Gender='M').count()
        y2013 = student.objects.filter(RegistrationStart='2013').filter(Qualified='F').filter(Gender='M').count()
        y2014 = student.objects.filter(RegistrationStart='2014').filter(Qualified='F').filter(Gender='M').count()
        y2015 = student.objects.filter(RegistrationStart='2015').filter(Qualified='F').filter(Gender='M').count()
        y2016 = student.objects.filter(RegistrationStart='2016').filter(Qualified='F').filter(Gender='M').count()
        y2017 = student.objects.filter(RegistrationStart='2017').filter(Qualified='F').filter(Gender='M').count()
        y2018 = student.objects.filter(RegistrationStart='2018').filter(Qualified='F').filter(Gender='M').count()


        self.assertEquals(y2008,0)
        self.assertEquals(y2009,0)
        self.assertEquals(y2010,0)
        self.assertEquals(y2011,0)
        self.assertEquals(y2012,0)
        self.assertEquals(y2013,0)
        self.assertEquals(y2014,0)
        self.assertEquals(y2015,1)
        self.assertEquals(y2016,2)
        self.assertEquals(y2017,0)
        self.assertEquals(y2018,2)










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
