from django import forms
from .models import Save

class CreateSaveForm(forms.ModelForm):

    class Meta:
        model = Save
        fields = ('name',)


class AdminCreateSave(forms.ModelForm):

    class Meta:
        model = Save
        fields = '__all__'


