from django.shortcuts import render

# Create your views here.

from .serializers import DetectorSerializer
from .models import Detector 
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

import os
from python_speech_features import mfcc
from python_speech_features import delta
import scipy.io.wavfile as wavy
import numpy as np
import tensorflow as tf
import keras
from keras.models import Model, load_model, Sequential
import pickle
from pydub import AudioSegment
#AudioSegment.ffprobe = "/usr/local/lib/python3.5/dist-packages/ffprobe-0.5.dist-info"


# Create your views here.

class DetectorView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        detector = Detector.objects.all()
        serializer = DetectorSerializer(detector, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        detector_serializer = DetectorSerializer(data=request.data)
        if detector_serializer.is_valid():
            detector_serializer.save()
            items = detector_serializer.validated_data

            file_name = items['file_name']
    
            sound = AudioSegment.from_mp3("./media/my_audios/" + file_name)
            sound.export("./media/my_audios_wav/" + file_name.split('.')[0] + ".wav", format="wav")

#            model = pickle.load(open('~/iiit/SEM 6/BTP/Stuttering/BTP_FP.sav', 'rb'))
            wav="./media/my_audios_wav/" + file_name.split('.')[0] + ".wav" ### Path of audio file
            newAudio = AudioSegment.from_wav(wav)
            (rate,sig) = wavy.read(wav)
            mfcc_feat = mfcc(sig,rate,numcep=15,nfilt=40,preemph=0.97)
            mfcc_d = delta(mfcc_feat,1)
            mfcc_dd = delta(mfcc_d,1)
            feat = np.concatenate((mfcc_feat,mfcc_d,mfcc_dd),axis=1)
            final_feats=[]
            
            for i in range(3,len(feat)-3):
                args = (feat[i-3],feat[i-2],feat[i-1],feat[i],feat[i+1],feat[i+2],feat[i+3])
                xt=[]
                xt = np.concatenate(args)
                final_feats.append(xt)
            
            final_feats = np.array(final_feats)
            return Response({'data': detector_serializer.data , 'features': final_feats})


#            yhat_classes = model.predict(final_feats)
#            a=0
#            kt=0
#            for i in range(len(yhat_classes)):
#                if yhat_classes[i]==1:
#                    a+=1
#                    if a==1:
#                        kt=i
#                elif a>0:
#                    k=0
#                    #print(i)
#                    j=i+1
#                    while j<=i+5 and j<len(yhat_classes):
#                        if yhat_classes[j]==1:
#                            k+=1
#                        j+=1
#                    if a<=28 and k<2:
#                        for j in range(kt,i):
#                            yhat_classes[j]=0
#                        a=0
#                    if k<2:
#                        a=0
#                    else:
#                        yhat_classes[i]=1
#            
#            print(yhat_classes) ### yhat_classes is an array of 1 and 0, in which 1 represents detected filled pause at that frame and 0 represents normal speech
### For conversion of yhat_classes to time array, each frame is of .01 seconds. And total no. of frames equal to total no. of elements in yhat_classes




            return Response(detector_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', detector_serializer.errors)
            return Response(detector_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
