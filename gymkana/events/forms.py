from django import forms
from .models import Event


class EventForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if end_date < start_date:
            raise forms.ValidationError("The end date can not be earlier than the start date")
        
        return cleaned_data
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type':'date'}),
            'end_date': forms.DateTimeInput(attrs={'type':'date'})

        }