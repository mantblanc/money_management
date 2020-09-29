from django import forms
from .models import MoneyTransaction

class MoneyForm(forms.ModelForm):
    class Meta:
        model = MoneyTransaction
        fields = ('entry_name', 'price', 'description')
