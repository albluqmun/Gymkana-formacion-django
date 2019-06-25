from django import forms
from .models import New
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    image = forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])], required=False)

    class Meta:
        model = New
        fields = ('id', 'title', 'image', 'subtitle', 'body',)
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        max_size=10*1024*1024

        if image and image.size > max_size:
            raise ValidationError("The maximum file size that can be uploaded is 10MB")

