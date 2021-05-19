from django import forms
from django.core.exceptions import ValidationError
from PIL import Image

from .models import New

class NewForm(forms.ModelForm):

    image = forms.ImageField(required=False)

    class Meta:
        model = New
        fields = ['title', 'subtitle', 'body', 'image']

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            format = Image.open(image).format
            if format not in ['JPEG', 'PNG']:
                raise ValidationError("Unsupported image type. Please upload jpeg or png.")
            elif image.size > 10485760:
                raise ValidationError("Uploaded image cannot be larger than 10MB of file size")
        return image

