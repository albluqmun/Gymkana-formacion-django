from django import forms
from .models import New, Event
from django.core.validators import FileExtensionValidator

class NewsForm(forms.ModelForm):

    def clean_image(self):

            image = self.cleaned_data['image']
            # esto es raro
            if type(image) != str:
                
                if image.size > (1024 * 1024 * 10):
                    raise forms.ValidationError("El tamaño de la imagen no debe superar los 10MB")
            return image

    class Meta:
        model = New    
        fields = ['title', 'subtitle', 'body', 'image']


class EventsForm(forms.ModelForm):

    class Meta:
        model = Event    
        fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']
