from django import forms
from voter.models import VoterModel

class VoterForm(forms.ModelForm):
    class Meta:
        model=VoterModel
        fields='__all__'
        