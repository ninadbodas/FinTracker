# forms.py
from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_date', 'amount', 'category', 'account', 'note', 'description']
        widgets = {
            'transaction_date': forms.DateInput(attrs={'class': 'admin-form-control' }),
            'amount': forms.NumberInput(attrs={'class': 'admin-form-control'}),
            'category': forms.Select(attrs={'class': 'admin-form-control responsive-field'}),
            'account': forms.TextInput(attrs={'class': 'admin-form-control responsive-field'}),
            'note': forms.TextInput(attrs={'class': 'admin-form-control responsive-field'}),
            'description': forms.Textarea(attrs={'class': 'admin-form-control responsive-field'}),
        }