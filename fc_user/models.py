from django.db import models
from django.contrib.auth.models import AbstractUser



class FilingCabinetUser(AbstractUser):
    display_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username
