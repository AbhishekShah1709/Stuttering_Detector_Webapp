from django.shortcuts import render

# Create your views here.

from .serializers import AudiofileSerializer
from .models import Audiofile
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AudiofileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        audiofiles = Audiofile.objects.all()
        serializer = AudiofileSerializer(audiofiles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        audiofiles_serializer = AudiofileSerializer(data=request.data)
        if audiofiles_serializer.is_valid():
            audiofiles_serializer.save()
            return Response(audiofiles_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', audiofiles_serializer.errors)
            return Response(audiofiles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
