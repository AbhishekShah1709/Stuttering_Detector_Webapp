from django.db import models

# Create your models here.

class Audiofile(models.Model):

    audio_name = models.TextField()
    audio_file = models.FileField(upload_to='my_audios/')
#    audio_name = models.CharField(max_length=100)
#    audio_file = models.FileField(upload_to='audio_player/')
#    audio_file = models.FileField(upload_to='audio_player/media/audio_player/')

#    content = models.TextField()
#    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.audio_name
