from django import forms
from .models import BusinessApplication

class BusinessApplicationForm(forms.ModelForm):
    """
    Form for creating and editing BusinessApplication objects.
    """
    class Meta:
        model = BusinessApplication
        fields = [
            'name',
            'appcode',
            'description',
            'owner',
            'delegate',
            'servicenow',
            'virtual_machines',
        ]
