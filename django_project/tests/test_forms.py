from django.test import SimpleTestCase
from accounts.forms import UserRegisterForm

#testing the UserRegistragionForm
class TestForms(SimpleTestCase):
    allow_database_queries = True
    
    def test_UserRegisterForm_valid_data(self):
        form = UserRegisterForm(data = {'username':"qwert04",
        'email':"coverCode@codegrinders.co.za",
        'password1':"thereispowerinunity",
        'password2':"thereispowerinunity"

        })
        self.assertTrue(form.is_valid())

    def test_UserRegisterForm_no_valid_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
