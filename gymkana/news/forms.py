from django import forms
from .models import New

class NewForm(forms.ModelForm):
    """
    TODO validacion imagen
    """
    def __init__(self, *args, **kwargs):
        super(NewForm, self).__init__(*args, **kwargs)
        # self.fields['image']
    model = New
    fields = '__all__'
