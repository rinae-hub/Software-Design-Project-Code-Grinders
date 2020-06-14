from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, GenerateGraphForm
from django.http import JsonResponse
from web.models import student


def ajax_generate_graph(request):
    if request.is_ajax():
        graph_type = request.POST.get('graph_type', False)
        dependent_variable = request.POST.get('dependent_variable', False)
        dependent_extra_variable = request.POST.get('dependent_variable_extra', False)
        colour_value = request.POST.get('colours', False)

        independent_values = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
        dependent_values = []
        dependent_values_1 = []

        '''Determination of first dependent variable'''
        if dependent_variable == 'Female and RegistrationEnd':
            y2008 = student.objects.filter(RegistrationEnd='2008').filter(Gender='F').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationEnd='2009').filter(Gender='F').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationEnd='2010').filter(Gender='F').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationEnd='2011').filter(Gender='F').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationEnd='2012').filter(Gender='F').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationEnd='2013').filter(Gender='F').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationEnd='2014').filter(Gender='F').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationEnd='2015').filter(Gender='F').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationEnd='2016').filter(Gender='F').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationEnd='2017').filter(Gender='F').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationEnd='2018').filter(Gender='F').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Male and RegistrationEnd':
            y2008 = student.objects.filter(RegistrationEnd='2008').filter(Gender='M').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationEnd='2009').filter(Gender='M').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationEnd='2010').filter(Gender='M').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationEnd='2011').filter(Gender='M').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationEnd='2012').filter(Gender='M').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationEnd='2013').filter(Gender='M').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationEnd='2014').filter(Gender='M').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationEnd='2015').filter(Gender='M').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationEnd='2016').filter(Gender='M').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationEnd='2017').filter(Gender='M').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationEnd='2018').filter(Gender='M').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Biological Science Degree':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(
                Streamline='Biological Science Degree').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Mathematics Degree':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Streamline='Mathematics Degree').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Physical Science Degree':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(
                Streamline='Physical Science Degree').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Earth Science Degree':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Streamline='Earth Science Degree').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Unknown Streamline':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Streamline='Unknown Streamline').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Female and Qualified':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Qualified='Q').filter(Gender='F').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Female and Not Qualified':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Qualified='F').filter(Gender='F').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Female and RegistrationStart':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Gender='F').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Gender='F').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Gender='F').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Gender='F').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Gender='F').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Gender='F').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Gender='F').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Gender='F').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Gender='F').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Gender='F').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Gender='F').count()
            dependent_values.append(y2018)

        elif dependent_variable == 'Male and RegistrationStart':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Gender='M').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Gender='M').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Gender='M').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Gender='M').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Gender='M').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Gender='M').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Gender='M').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Gender='M').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Gender='M').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Gender='M').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Gender='M').count()
            dependent_values.append(y2018)

            '''Number of students registered each year'''

        elif dependent_variable == 'RegistrationStart':
            y2008 = student.objects.filter(RegistrationStart='2008').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').count()
            dependent_values.append(y2018)

            '''Number of students deregistered each year'''

        elif dependent_variable == 'RegistrationEnd':
            y2008 = student.objects.filter(RegistrationEnd='2008').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationEnd='2009').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationEnd='2010').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationEnd='2011').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationEnd='2012').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationEnd='2013').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationEnd='2014').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationEnd='2015').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationEnd='2016').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationEnd='2017').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationEnd='2018').count()
            dependent_values.append(y2018)

            '''Number of first year students registered each year'''

        elif dependent_variable == 'YearStarted':
            y2008 = student.objects.filter(YearStarted='2008').count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(YearStarted='2009').count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(YearStarted='2010').count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(YearStarted='2011').count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(YearStarted='2012').count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(YearStarted='2013').count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(YearStarted='2014').count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(YearStarted='2015').count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(YearStarted='2016').count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(YearStarted='2017').count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(YearStarted='2018').count()
            dependent_values.append(y2018)

            '''Determination of second dependent variable'''

        elif dependent_variable == 'No Student Record':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Nostudentrrecord=1).count()
            dependent_values.append(y2018)

        # *************************************************************************************************** #
        if dependent_extra_variable == 'Female and RegistrationEnd':
            y2008 = student.objects.filter(RegistrationEnd='2008').filter(Gender='F').count()
            dependent_values_1.append(y2008)

            y2009 = student.objects.filter(RegistrationEnd='2009').filter(Gender='F').count()
            dependent_values_1.append(y2009)

            y2010 = student.objects.filter(RegistrationEnd='2010').filter(Gender='F').count()
            dependent_values_1.append(y2010)

            y2011 = student.objects.filter(RegistrationEnd='2011').filter(Gender='F').count()
            dependent_values_1.append(y2011)

            y2012 = student.objects.filter(RegistrationEnd='2012').filter(Gender='F').count()
            dependent_values_1.append(y2012)

            y2013 = student.objects.filter(RegistrationEnd='2013').filter(Gender='F').count()
            dependent_values_1.append(y2013)

            y2014 = student.objects.filter(RegistrationEnd='2014').filter(Gender='F').count()
            dependent_values_1.append(y2014)

            y2015 = student.objects.filter(RegistrationEnd='2015').filter(Gender='F').count()
            dependent_values_1.append(y2015)

            y2016 = student.objects.filter(RegistrationEnd='2016').filter(Gender='F').count()
            dependent_values_1.append(y2016)

            y2017 = student.objects.filter(RegistrationEnd='2017').filter(Gender='F').count()
            dependent_values_1.append(y2017)

            y2018 = student.objects.filter(RegistrationEnd='2018').filter(Gender='F').count()
            dependent_values_1.append(y2018)

        elif dependent_extra_variable == 'Male and RegistrationEnd':
            y2008 = student.objects.filter(RegistrationEnd='2008').filter(Gender='M').count()
            dependent_values_1.append(y2008)

            y2009 = student.objects.filter(RegistrationEnd='2009').filter(Gender='M').count()
            dependent_values_1.append(y2009)

            y2010 = student.objects.filter(RegistrationEnd='2010').filter(Gender='M').count()
            dependent_values_1.append(y2010)

            y2011 = student.objects.filter(RegistrationEnd='2011').filter(Gender='M').count()
            dependent_values_1.append(y2011)

            y2012 = student.objects.filter(RegistrationEnd='2012').filter(Gender='M').count()
            dependent_values_1.append(y2012)

            y2013 = student.objects.filter(RegistrationEnd='2013').filter(Gender='M').count()
            dependent_values_1.append(y2013)

            y2014 = student.objects.filter(RegistrationEnd='2014').filter(Gender='M').count()
            dependent_values_1.append(y2014)

            y2015 = student.objects.filter(RegistrationEnd='2015').filter(Gender='M').count()
            dependent_values_1.append(y2015)

            y2016 = student.objects.filter(RegistrationEnd='2016').filter(Gender='M').count()
            dependent_values_1.append(y2016)

            y2017 = student.objects.filter(RegistrationEnd='2017').filter(Gender='M').count()
            dependent_values_1.append(y2017)

            y2018 = student.objects.filter(RegistrationEnd='2018').filter(Gender='M').count()
            dependent_values_1.append(y2018)

        elif dependent_extra_variable == 'Female and RegistrationStart':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Gender='F').count()
            dependent_values_1.append(y2008)

            y2009 = student.objects.filter(RegistrationStart='2009').filter(Gender='F').count()
            dependent_values_1.append(y2009)

            y2010 = student.objects.filter(RegistrationStart='2010').filter(Gender='F').count()
            dependent_values_1.append(y2010)

            y2011 = student.objects.filter(RegistrationStart='2011').filter(Gender='F').count()
            dependent_values_1.append(y2011)

            y2012 = student.objects.filter(RegistrationStart='2012').filter(Gender='F').count()
            dependent_values_1.append(y2012)

            y2013 = student.objects.filter(RegistrationStart='2013').filter(Gender='F').count()
            dependent_values_1.append(y2013)

            y2014 = student.objects.filter(RegistrationStart='2014').filter(Gender='F').count()
            dependent_values_1.append(y2014)

            y2015 = student.objects.filter(RegistrationStart='2015').filter(Gender='F').count()
            dependent_values_1.append(y2015)

            y2016 = student.objects.filter(RegistrationStart='2016').filter(Gender='F').count()
            dependent_values_1.append(y2016)

            y2017 = student.objects.filter(RegistrationStart='2017').filter(Gender='F').count()
            dependent_values_1.append(y2017)

            y2018 = student.objects.filter(RegistrationStart='2018').filter(Gender='F').count()
            dependent_values_1.append(y2018)

        elif dependent_extra_variable == 'Male and RegistrationStart':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Gender='M').count()
            dependent_values_1.append(y2008)

            y2009 = student.objects.filter(RegistrationStart='2009').filter(Gender='M').count()
            dependent_values_1.append(y2009)

            y2010 = student.objects.filter(RegistrationStart='2010').filter(Gender='M').count()
            dependent_values_1.append(y2010)

            y2011 = student.objects.filter(RegistrationStart='2011').filter(Gender='M').count()
            dependent_values_1.append(y2011)

            y2012 = student.objects.filter(RegistrationStart='2012').filter(Gender='M').count()
            dependent_values_1.append(y2012)

            y2013 = student.objects.filter(RegistrationStart='2013').filter(Gender='M').count()
            dependent_values_1.append(y2013)

            y2014 = student.objects.filter(RegistrationStart='2014').filter(Gender='M').count()
            dependent_values_1.append(y2014)

            y2015 = student.objects.filter(RegistrationStart='2015').filter(Gender='M').count()
            dependent_values_1.append(y2015)

            y2016 = student.objects.filter(RegistrationStart='2016').filter(Gender='M').count()
            dependent_values_1.append(y2016)

            y2017 = student.objects.filter(RegistrationStart='2017').filter(Gender='M').count()
            dependent_values_1.append(y2017)

            y2018 = student.objects.filter(RegistrationStart='2018').filter(Gender='M').count()
            dependent_values_1.append(y2018)

            '''Number of students registered each year'''

        elif dependent_extra_variable == 'RegistrationStart':
            y2008 = student.objects.filter(RegistrationStart='2008').count()
            dependent_values_1.append(y2008)

            y2009 = student.objects.filter(RegistrationStart='2009').count()
            dependent_values_1.append(y2009)

            y2010 = student.objects.filter(RegistrationStart='2010').count()
            dependent_values_1.append(y2010)

            y2011 = student.objects.filter(RegistrationStart='2011').count()
            dependent_values_1.append(y2011)

            y2012 = student.objects.filter(RegistrationStart='2012').count()
            dependent_values_1.append(y2012)

            y2013 = student.objects.filter(RegistrationStart='2013').count()
            dependent_values_1.append(y2013)

            y2014 = student.objects.filter(RegistrationStart='2014').count()
            dependent_values_1.append(y2014)

            y2015 = student.objects.filter(RegistrationStart='2015').count()
            dependent_values_1.append(y2015)

            y2016 = student.objects.filter(RegistrationStart='2016').count()
            dependent_values_1.append(y2016)

            y2017 = student.objects.filter(RegistrationStart='2017').count()
            dependent_values_1.append(y2017)

            y2018 = student.objects.filter(RegistrationStart='2018').count()
            dependent_values_1.append(y2018)

            '''Number of students deregistered each year'''

        elif dependent_extra_variable == 'RegistrationEnd':
            y2008 = student.objects.filter(RegistrationEnd='2008').count()
            dependent_values_1.append(y2008)

            y2009 = student.objects.filter(RegistrationEnd='2009').count()
            dependent_values_1.append(y2009)
            y2010 = student.objects.filter(RegistrationEnd='2010').count()
            dependent_values_1.append(y2010)

            y2011 = student.objects.filter(RegistrationEnd='2011').count()
            dependent_values_1.append(y2011)

            y2012 = student.objects.filter(RegistrationEnd='2012').count()
            dependent_values_1.append(y2012)

            y2013 = student.objects.filter(RegistrationEnd='2013').count()
            dependent_values_1.append(y2013)

            y2014 = student.objects.filter(RegistrationEnd='2014').count()
            dependent_values_1.append(y2014)

            y2015 = student.objects.filter(RegistrationEnd='2015').count()
            dependent_values_1.append(y2015)

            y2016 = student.objects.filter(RegistrationEnd='2016').count()
            dependent_values_1.append(y2016)

            y2017 = student.objects.filter(RegistrationEnd='2017').count()
            dependent_values_1.append(y2017)

            y2018 = student.objects.filter(RegistrationEnd='2018').count()
            dependent_values_1.append(y2018)

            '''Number of first year students registered each year'''

        elif dependent_extra_variable == 'YearStarted':
            y2008 = student.objects.filter(YearStarted='2008').count()
            dependent_values_1.append(y2008)

            y2009 = student.objects.filter(YearStarted='2009').count()
            dependent_values_1.append(y2009)

            y2010 = student.objects.filter(YearStarted='2010').count()
            dependent_values_1.append(y2010)

            y2011 = student.objects.filter(YearStarted='2011').count()
            dependent_values_1.append(y2011)

            y2012 = student.objects.filter(YearStarted='2012').count()
            dependent_values_1.append(y2012)

            y2013 = student.objects.filter(YearStarted='2013').count()
            dependent_values_1.append(y2013)

            y2014 = student.objects.filter(YearStarted='2014').count()
            dependent_values_1.append(y2014)

            y2015 = student.objects.filter(YearStarted='2015').count()
            dependent_values_1.append(y2015)

            y2016 = student.objects.filter(YearStarted='2016').count()
            dependent_values_1.append(y2016)

            y2017 = student.objects.filter(YearStarted='2017').count()
            dependent_values_1.append(y2017)

            y2018 = student.objects.filter(YearStarted='2018').count()
            dependent_values_1.append(y2018)

        elif dependent_extra_variable == 'Male and Qualified':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Qualified='Q').filter(Gender='M').count()
            dependent_values_1.append(y2018)

        elif dependent_extra_variable == 'Male and Not Qualified':
            y2008 = student.objects.filter(RegistrationStart='2008').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2008)
            y2009 = student.objects.filter(RegistrationStart='2009').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2009)
            y2010 = student.objects.filter(RegistrationStart='2010').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2010)
            y2011 = student.objects.filter(RegistrationStart='2011').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2011)
            y2012 = student.objects.filter(RegistrationStart='2012').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2012)
            y2013 = student.objects.filter(RegistrationStart='2013').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2013)
            y2014 = student.objects.filter(RegistrationStart='2014').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2014)
            y2015 = student.objects.filter(RegistrationStart='2015').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2015)
            y2016 = student.objects.filter(RegistrationStart='2016').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2016)
            y2017 = student.objects.filter(RegistrationStart='2017').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2017)
            y2018 = student.objects.filter(RegistrationStart='2018').filter(Qualified='F').filter(Gender='M').count()
            dependent_values_1.append(y2018)

        '''Determination of graph labels '''

        label0 = 'label'
        label1 = 'label'
        if dependent_variable == 'RegistrationStart':
            label0 = 'Number of Registered Students'
        elif dependent_variable == 'RegistrationEnd':
            label0 = 'Number of Deregistered Students'
        elif dependent_variable == 'YearStarted':
            label0 = 'Number of First Year Students - UG OR PG'
        elif dependent_variable == 'Female and RegistrationStart':
            label0 = 'Number of Female Registered Students'
        elif dependent_variable == 'Female and RegistrationEnd':
            label0 = 'Number of Female Deregistered Students'
        elif dependent_variable == 'Biological Science Degree':
            label0 = 'Number in Biological Science Degree'
        elif dependent_variable == 'Mathematics Degree':
            label0 = 'Number in Mathematics Degree'
        elif dependent_variable == 'Physical Science Degree':
            label0 = 'Physical Science Degree'
        elif dependent_variable == 'Earth Science Degree':
            label0 = 'Earth Science Degree'
        elif dependent_variable == 'Unknown Streamline':
            label0 = 'Unknown Streamline'
        elif dependent_variable == 'Female and Qualified':
            label0 = 'Female and Qualified'
        elif dependent_variable == 'Female and Not Qualified':
            label0 = 'Female and Not Qualified'
        elif dependent_variable == 'No Student Record':
            label0 = 'No Student Record'

        if dependent_extra_variable == 'RegistrationStart':
            label1 = 'Number of Registered Students'
        elif dependent_extra_variable == 'RegistrationEnd':
            label1 = 'Number of Deregistered Students'
        elif dependent_extra_variable == 'YearStarted':
            label1 = 'Number of First Year Students - UG OR PG'
        elif dependent_extra_variable == 'Male and RegistrationStart':
            label1 = 'Number of Male Registered Students'
        elif dependent_extra_variable == 'Male and RegistrationEnd':
            label1 = 'Number of Male deregistered Students'
        elif dependent_extra_variable == 'Male and Qualified':
            label1 = 'Male and Qualified'
        elif dependent_extra_variable == 'Male and Not Qualified':
            label1 = 'Male and Not Qualified'

        graphinfo = {
            "independent_values": independent_values,
            "dependent_values": dependent_values,
            "dependent_extra_values": dependent_values_1,
            "graph_type": graph_type,
            "colours": colour_value,
            "name_1": label0,
            "name_2": label1
        }

        return JsonResponse(graphinfo)


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})  # templates


def graph(request, *args, **kwargs):
    form = GenerateGraphForm()
    return render(request, "graph.html", {'form': form})  # templates


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:

        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def redirect_view(request):
    response = redirect('')
    return response
