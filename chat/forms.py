from django import forms
from django.db import models 

class ConnectForm(forms.Form):

    #class Meta:
    #    model = MyModel

    users = [
        (0, 'nobody'),
    ]

    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('users')
        super(ConnectForm, self).__init__(*args, **kwargs)
        self.fields['pair'].choices = self.users

    def new_choices(self, *args, **kwargs):
        self.users = kwargs.pop('users')
        super(ConnectForm, self).__init__(*args, **kwargs)
        self.fields['pair'].choices = self.users

    #name = forms.CharField(label='Choose your name')
    pair = forms.ChoiceField(choices=users)

