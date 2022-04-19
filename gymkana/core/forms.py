from django import forms
from .models import New, Event
from django.core.validators import FileExtensionValidator

class NewsForm(forms.ModelForm):

    class Meta:
        
        model = New    
        fields = ['title', 'subtitle', 'body', 'image']

     # validacion de extensiones de archivos
    



