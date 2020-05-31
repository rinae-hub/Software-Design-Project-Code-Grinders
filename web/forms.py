from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

independent = [('years', 'Years')]
graphs = [('bar', 'Bar-Graph'),
          ('pie', 'Pie-Chart'),
          ('lines', 'Line-Graph'),
          ('scatter', 'Scatter-Plot'),
          ('sunburst', 'Sunburst'),
          ('markers', 'Bubble Chart')
          ]
dependent = [
    ('RegistrationStart', 'Registered Students'),
    ('RegistrationEnd', 'Deregistered Students'),
    ('YearStarted', 'First Year Students - UG OR PG'),
    ('Male and RegistrationStart', 'Male Registered Students'),
    ('Female and RegistrationStart', 'Female Registered Students'),
    ('Male and RegistrationEnd', 'Male Deregistered Students'),
    ('Female and RegistrationEnd', 'Female Deregistered Students'),
]
dependent_extras = [
    ('Black', ''),
    ('RegistrationStart', 'Registered Students'),
    ('RegistrationEnd', 'Deregistered Students'),
    ('YearStarted', 'First Year Students - UG OR PG'),
    ('Male and RegistrationStart', 'Male Registered Students'),
    ('Female and RegistrationStart', 'Female Registered Students'),
    ('Male and RegistrationEnd', 'Male Deregistered Students'),
    ('Female and RegistrationEnd', 'Female Deregistered Students'),
]

colour = [('#00FF00', 'Green'),
          ('#0000FF', 'Blue'),
          ('#800000', 'Maroon'),
          ('#FFFF00', 'Yellow'),
          ('#808000', 'Olive'),
          ('#00FF00', 'Lime'),
          ]


class GenerateGraphForm(forms.Form):
    independent_variable = forms.CharField(required=True, widget=forms.Select(choices=independent))
    dependent_variable = forms.CharField(required=True, widget=forms.Select(choices=dependent))
    dependent_variable_extra = forms.CharField(widget=forms.Select(choices=dependent_extras))
    colours = forms.CharField(widget=forms.Select(choices=colour))
    graph_type = forms.CharField(max_length=3, widget=forms.Select(choices=graphs))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
