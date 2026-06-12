from django import forms
from .models import Transaction, Category

class CategoryForm(forms.ModelForm):
    """Formularz służący do tworzenia i edycji kategorii."""
    class Meta:
        model = Category
        fields = ['name', 'type']

class TransactionForm(forms.ModelForm):
    """Formularz służący do obsługi transakcji finansowych."""
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'description', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        """
        Inicjalizuje formularz, filtrując listę dostępnych kategorii 
        tak, aby użytkownik widział tylko swoje własne kategorie.
        """
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = self.fields['category'].queryset.filter(user=user)
