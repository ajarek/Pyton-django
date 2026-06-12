from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Formularz służący do tworzenia konta nowego użytkownika (CustomUser)."""
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    """Formularz służący do edycji danych istniejącego użytkownika."""
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
