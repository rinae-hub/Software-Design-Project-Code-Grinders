from django.test import TestCase
from web.forms import UserRegisterForm

class TestForms(TestCase):

    def test_registerform_valid_data(self):
        form = UserRegisterForm(data={
        'username' : 'TAS',
        'email':'google2020@gmail.com',
        'password1':'124ther_lamsT',
        'password2':'124ther_lamsT'
        })
        self.assertTrue(form.is_valid())

    def test_registerform_no_data(self):
        form =UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
