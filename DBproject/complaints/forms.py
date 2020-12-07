from django import forms
from .models import Complain


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ['customer_ID', 'date', 'complain_type', 'room_number', 'employee_ID', 'problem_type', 'complain_message', ]
