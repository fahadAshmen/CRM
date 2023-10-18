from . models import Lead
from django import forms

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name','description','email','priority','status']