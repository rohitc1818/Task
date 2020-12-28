from django import forms
from gooApp.models import Info

# create your form here.
class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = "__all__"



