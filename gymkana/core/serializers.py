from rest_framework import serializers
from .models import *

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'subtitle', 'body', 'image')

    # validate image size
    def validate_image(self, value):
        if value.size > (1024 * 1024 * 10):
            raise serializers.ValidationError("El tamaño de la imagen no debe superar los 10MB")
        return value

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'subtitle', 'body', 'start_date', 'end_date')