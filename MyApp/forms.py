from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense

        fields = ['expense_name', 'category', 'amount', 'date', 'payment_method', 'notes',]

        widgets = {
            'expense_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: Lunch'}),

            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: Food, Transportation, School'}),

            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount', 'step': '0.01','min': '0'}),

            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'payment_method': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: Cash, GCash, Bank'}),

            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Optional notes','rows': 4}),
        }