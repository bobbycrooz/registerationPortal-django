from django import forms
from userLoginApp.models import userFrofileInfo

#defining the form input
class userRegForm(forms.ModelForm):
    #make passwordfield a password format
    password = forms.CharField(widget=forms.PasswordInput())

    #get fields from form
    class Meta():
        model = userFrofileInfo
        fields = ('firstname', 'lastname', 'email', 'password')

