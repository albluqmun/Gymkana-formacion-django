from rest_framework import serializers
from .models import *

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'subtitle', 'body', 'image')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'subtitle', 'body', 'start_date', 'end_date')