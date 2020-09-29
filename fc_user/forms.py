from django import forms
from fc_user.models import FilingCabinetUser
from django.contrib.auth.forms import UserCreationForm


class FCUserForm(UserCreationForm):
    class META:
        model = FilingCabinetUser
        fields = ('display_name')