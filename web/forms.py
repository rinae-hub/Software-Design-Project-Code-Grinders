from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

independent = [('years', 'Years')]
graphs = [('bar', 'bar'),
          ('pie', 'pie'),
          ('line', 'Line'),
          ('radar', 'radar'),
          ('polarArea', 'polarArea'),
          ]
dependent = [
    ('RegistrationStart', 'Registered Students'),
    ('RegistrationEnd', 'Deregistered Students'),
    ('YearStarted', 'First Year Students - UG OR PG'),
    ('Biological Science Degree', 'Biological Science Degree'),
    ('Mathematics Degree', 'Mathematics Degree'),
    ('Physical Science Degree', 'Physical Science Degree'),
    ('Earth Science Degree', 'Earth Science Degree'),
    ('Unknown Streamline', 'Unknown Streamline'),
    ('Female and RegistrationStart', 'Female Registered Students'),
    ('Female and RegistrationEnd', 'Female Deregistered Students'),
    ('Female and Qualified', 'Female and Qualified'),
    ('Female and Not Qualified', 'Female and Not Qualified'),


]
dependent_extras = [
    ('Black', ''),
    ('Male and RegistrationStart', 'Male Registered Students'),
    ('Male and RegistrationEnd', 'Male Deregistered Students'),
    ('Male and Qualified', 'Male and Qualified'),
    ('Male and Not Qualified', 'Male and Not Qualified'),

]

class GenerateGraphForm(forms.Form):
    independent_variable = forms.CharField(required=True,widget=forms.Select(choices=independent))
    dependent_variable_female = forms.CharField(required=True,widget=forms.Select(choices=dependent))
    dependent_variable_male =forms.CharField(widget=forms.Select(choices=dependent_extras))
    graph_type = forms.CharField(widget=forms.Select(choices=graphs))



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
