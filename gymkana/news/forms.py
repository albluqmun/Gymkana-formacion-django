from django import forms
from .models import New
from django.core.exceptions import ValidationError
from .validators import image_extension, image_size


class NewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewForm, self).__init__(*args, **kwargs)

    """
    def clean(self):
        cleaned_data = super(NewForm, self).clean()
        # import ipdb; ipdb.set_trace()
        image = cleaned_data.get('image')
        #image_extension(image)
        print(image)
        image_size(image)
    """   

    class Meta:
        model = New
        fields = '__all__'


    
    

