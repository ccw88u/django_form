from django import forms
from form_basic.models import Reguser


class ReguserForm(forms.ModelForm):
    class Meta:
        model = Reguser
        fields = '__all__'