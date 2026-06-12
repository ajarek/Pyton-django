from django.db import models
from django.conf import settings

class Category(models.Model):
    """
    Reprezentuje kategorię transakcji (np. Jedzenie, Wynagrodzenie).
    Kategorie są przypisane do konkretnego użytkownika i mają określony typ (Przychód/Wydatek).
    """
    TYPE_CHOICES = (
        ('INCOME', 'Przychód'),
        ('EXPENSE', 'Wydatek'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """Zwraca czytelną reprezentację kategorii."""
        return f"{self.name} ({self.get_type_display()})"

class Transaction(models.Model):
    """
    Reprezentuje pojedynczą operację finansową (transakcję).
    Przechowuje kwotę, datę, opis oraz powiązanie z kategorią i użytkownikiem.
    """
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """Zwraca czytelną reprezentację transakcji."""
        return f"{self.date} - {self.category.name}: {self.amount:.2f}"
