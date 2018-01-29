from django import forms
from form_basic.models import Reguser, website
#from django.forms.extras.widgets import SelectDateWidget
#from django.contrib.admin import widgets  

class ReguserForm(forms.ModelForm):
    class Meta:
        model = Reguser
        fields = '__all__'

class websiteForm(forms.ModelForm):
    
    class Meta:
        model = website
        fields = '__all__'

