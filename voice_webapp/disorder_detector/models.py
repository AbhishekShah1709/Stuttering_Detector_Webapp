from django.db import models

# Create your models here.

class Detector(models.Model):

    file_name = models.TextField(blank=True, null=True)
    file_details = models.FileField(upload_to='tmp/', blank=True, null=True)
    blob_details = models.BinaryField(editable=True, blank=True, null=True)
    category = models.TextField(blank=True, null=True)
#    audio_name = models.CharField(max_length=100)
#    audio_file = models.FileField(upload_to='audio_player/')
#    audio_file = models.FileField(upload_to='audio_player/media/audio_player/')

#    content = models.TextField()
#    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.file_name
