from django.urls import path
from . import views

urlpatterns = [
    path('disorder_detection/', views.DetectorView.as_view(), name= 'detector_list'),
]
