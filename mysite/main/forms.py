'''
Forms file
'''

from django import forms

class CreateNewList(forms.Form):
    '''
    Form for creating a new list
    '''
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
