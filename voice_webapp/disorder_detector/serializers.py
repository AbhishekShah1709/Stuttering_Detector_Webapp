from rest_framework import serializers
from .models import Detector 

class DetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector 
        fields = '__all__'
