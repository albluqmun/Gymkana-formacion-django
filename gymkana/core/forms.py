from django import forms
from .models import New, Event
from django.core.validators import FileExtensionValidator

class NewsForm(forms.ModelForm):

    class Meta:
        model = New    
        fields = ['title', 'subtitle', 'body', 'image']

    def clean_image(self):

            image = self.cleaned_data['image']
            # esto es raro
            if type(image) != str:
                
                if image.size > (1024 * 1024 * 10):
                    raise forms.ValidationError("El tamaño de la imagen no debe superar los 10MB")
            return image


class EventsForm(forms.ModelForm):

    class Meta:
        model = Event    
        fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']
    
    def clean(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if start_date > end_date:
            raise forms.ValidationError("La fecha de inicio debe ser menor a la fecha de fin")
