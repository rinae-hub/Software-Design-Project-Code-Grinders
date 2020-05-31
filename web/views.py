from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, GenerateGraphForm
from django.http import JsonResponse
from web.models import student


def ajax_generate_graph(request):
    if request.method == 'POST':
        graph_type = request.POST['graph_type']
        independent_variable = request.POST['independent_variable']
        dependent_variable = request.POST['dependent_variable']
        dependent_extra_variable = request.POST['dependent_variable_extra']
        colour_value = request.POST['colours']

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

        '''Determination of graph labels '''

        label0 = 'label'
        label1 = 'label'
        if dependent_variable == 'RegistrationStart':
            label0 = 'Number of Registered Students'
        elif dependent_variable == 'RegistrationEnd':
            label0 = 'Number of Deregistered Students'
        elif dependent_variable == 'YearStarted':
            label0 = 'Number of First Year Students - UG OR PG'
        elif dependent_variable == 'Male and RegistrationStart':
            label0 = 'Number of Male Registered Students'
        elif dependent_variable == 'Female and RegistrationStart':
            label0 = 'Number of Female Registered Students'
        elif dependent_variable == 'Male and RegistrationEnd':
            label0 = 'Number of Male Deregistered Students'
        elif dependent_variable == 'Female and RegistrationEnd':
            label0 = 'Number of Female Deregistered Students'

        if dependent_extra_variable == 'RegistrationStart':
            label1 = 'Number of Registered Students'
        elif dependent_extra_variable == 'RegistrationEnd':
            label1 = 'Number of Deregistered Students'
        elif dependent_extra_variable == 'YearStarted':
            label1 = 'Number of First Year Students - UG OR PG'
        elif dependent_extra_variable == 'Male and RegistrationStart':
            label1 = 'Number of Male Registered Students'
        elif dependent_extra_variable == 'Female and RegistrationStart':
            label1 = 'Number of Female Registered Students'
        elif dependent_extra_variable == 'Male and RegistrationEnd':
            label1 = 'Number of Male deregistered Students'
        elif dependent_extra_variable == 'Female and RegistrationEnd':
            label1 = 'Number of Female deregistered Students'

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


def abc(request, *args, **kwargs):
    return render(request, "abc.html", {})  # templates


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
    response = redirect('home/')
    return response
