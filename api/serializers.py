#api/serializers.py
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    # dateLastUpdate = serializers.DateField()
    # dateLastUpdate = serializers.DateField(format=None, input_formats=api_settings.DATETIME_FORMAT)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Event
        # fields = ('id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy' )
        fields = '__all__'
        
        # read_only_fields = ('date_created', 'date_modified')