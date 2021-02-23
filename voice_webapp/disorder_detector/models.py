from django.db import models

# Create your models here.

class Detector(models.Model):

    file_name = models.TextField()
    file_details = models.FileField()
#    audio_name = models.CharField(max_length=100)
#    audio_file = models.FileField(upload_to='audio_player/')
#    audio_file = models.FileField(upload_to='audio_player/media/audio_player/')

#    content = models.TextField()
#    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.file_name
