from django import forms
from .models import Account,Profile,Nickname,Name,Sns,Proof

class UploadProfile(forms.ModelForm) : 
    class Meta : 
        model = Profile
        fields = {'puuid','url'}