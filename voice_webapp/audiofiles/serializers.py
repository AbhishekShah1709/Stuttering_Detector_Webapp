from rest_framework import serializers
from .models import Audiofile 

class AudiofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiofile
        fields = '__all__'
