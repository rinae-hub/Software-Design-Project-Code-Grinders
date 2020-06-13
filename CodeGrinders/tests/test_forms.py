from django.test import TestCase
from web.forms import UserRegisterForm, GenerateGraphForm

'''
class GenerateGraphForm(forms.Form):
    independent_variable = forms.CharField(required=True,widget=forms.Select(choices=independent))
    dependent_variable = forms.CharField(required=True,widget=forms.Select(choices=dependent))
    dependent_variable_extra =forms.CharField(widget=forms.Select(choices=dependent_extras))
    colours =forms.CharField(widget=forms.Select(choices=colour))
    graph_type = forms.CharField(max_length=3,widget=forms.Select(choices=graphs))
'''
class TestForms(TestCase):

    #testing the registrationform with data
    def test_registerform_valid_data(self):
        form = UserRegisterForm(data={'username' : 'TAS','email':'google2020@gmail.com','password1':'124ther_lamsT','password2':'124ther_lamsT'})
        self.assertTrue(form.is_valid())

    #testing the registrationform with no data
    def test_registerform_no_data(self):
        form =UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)

    #testing the GenerateGraphForm with valid data
    def test_graphform_valid_data(self):
        form = GenerateGraphForm(data={'independent_variable':'Years','dependent_variable':'Registered Students','dependent_variable_extra':'Registered Students','colours':'Blue','graph_type':'Bar-Graph'})
        self.assertTrue(form.is_valid())

    #testing the GenerateGraphForm with no valid data
    def test_graphform_valid_no_data(self):
        form =GenerateGraphForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),5)
