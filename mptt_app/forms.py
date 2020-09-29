from django import forms
from mptt_app.models import FilingCabinet
from mptt.forms import TreeNodeChoiceField


class FolderFileForm(forms.Form):
    name = forms.CharField(max_length=100)
    parent = TreeNodeChoiceField(queryset=FilingCabinet.objects.all())