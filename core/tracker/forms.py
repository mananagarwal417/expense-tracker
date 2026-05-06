from django import forms
from .models import Category, Transaction

class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'e.g. Grocery shopping'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control', 'placeholder': '0.00', 'min': '0', 'step': '0.01'})
        self.fields['date'].widget.attrs.update({'class': 'form-control'})

        self.fields['category'].queryset = Category.objects.order_by('name')
        self.fields['category'].empty_label = 'Select category'
        self.fields['category'].widget.attrs.update({'class': 'form-select'})

        self.fields['transaction_type'].choices = [('', 'Select transaction type')] + list(Transaction.TYPES)
        self.fields['transaction_type'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'category', 'transaction_type', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }