from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Niestandardowy model użytkownika rozszerzający wbudowany model Django AbstractUser.
    Pozwala na łatwe dodawanie dodatkowych pól w przyszłości.
    """
    pass
