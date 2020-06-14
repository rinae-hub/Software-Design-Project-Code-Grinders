from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

independent = [('years', 'Years')]
graphs = [('bar', 'Bar-Graph'),
          ('pie', 'Pie-Chart'),
          ('lines', 'Line-Graph'),
          ('scatter', 'Scatter-Plot'),
          ('sunburst', 'Sunburst'),
          ('markers', 'Bubble Chart'),
          ('polar','Polar Chart')
          ]
dependent = [
    ('RegistrationStart', 'Registered Students'),
    ('RegistrationEnd', 'Deregistered Students'),
    ('YearStarted', 'First Year Students - UG OR PG'),
    ('Female and RegistrationStart', 'Female Registered Students'),
    ('Female and RegistrationEnd', 'Female Deregistered Students'),
    ('Biological Science Degree', 'Biological Science Degree'),
    ('Mathematics Degree', 'Mathematics Degree'),
    ('Physical Science Degree', 'Physical Science Degree'),
    ('Earth Science Degree', 'Earth Science Degree'),
    ('Unknown Streamline', 'Unknown Streamline'),
    ('Female and Qualified', 'Female and Qualified'),
    ('Female and Not Qualified', 'Female and Not Qualified'),
    ('No Student Record', 'No Student Record'),

]
dependent_extras = [
    ('Black', ''),
    ('Male and RegistrationStart', 'Male Registered Students'),
    ('Male and RegistrationEnd', 'Male Deregistered Students'),
    ('Male and Qualified', 'Male and Qualified'),
    ('Male and Not Qualified', 'Male and Not Qualified'),

]
colour = [('#00FF00', 'Green'),
          ('#0000FF', 'Blue'),
          ('#800000', 'Maroon'),
          ('#FFFF00', 'Yellow'),
          ('#808000', 'Olive'),
          ('#00FF00', 'Lime'),
          ]

class GenerateGraphForm(forms.Form):
    independent_variable = forms.CharField(required=True,widget=forms.Select(choices=independent))
    dependent_variable = forms.CharField(required=True,widget=forms.Select(choices=dependent))
    dependent_variable_extra =forms.CharField(widget=forms.Select(choices=dependent_extras))
    colours =forms.CharField(widget=forms.Select(choices=colour))
    graph_type = forms.CharField(widget=forms.Select(choices=graphs))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
