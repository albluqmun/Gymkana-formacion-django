from rest_framework import serializers
from rest_framework.fields import DateField
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError("The end date can not be earlier than the start date")
        return data


    def __init__(self, *args, **kwargs):
        super(EventSerializer, self).__init__(*args, **kwargs)


    def clean(self):

        cleaned_data = super(EventSerializer, self).clean()
        return cleaned_data


    class Meta:
        model = Event
        fields = '__all__'

        