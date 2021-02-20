from django.urls import path
from . import views

urlpatterns = [
    path('audiofiles/', views.AudiofileView.as_view(), name= 'audiofiles_list'),
]
