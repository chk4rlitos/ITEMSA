from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from django.conf import settings


class LoginForm(forms.Form):
    nick = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    llave = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': u'Contraseña'}))


    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-10'
        return helper