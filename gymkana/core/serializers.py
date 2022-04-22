from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'subtitle', 'body', 'start_date', 'end_date')

    # validate start_date and end_date
    def validate(self, data):
        start_date = data['start_date']
        end_date = data['end_date']
        if start_date > end_date:
            raise serializers.ValidationError("La fecha de inicio debe ser menor a la fecha de fin")
        return data