from django import forms
from mptt_app.models import FilingCabinet
from fc_user.models import FilingCabinetUser
from mptt.forms import TreeNodeChoiceField



class FolderFileForm(forms.ModelForm):
    class Meta:
        model = FilingCabinet
        fields = ('name', 'parent')


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = FilingCabinetUser
        fields = ["display_name"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)