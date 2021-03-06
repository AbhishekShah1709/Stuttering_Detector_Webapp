from django.db import models

#def user_directory_path(instance, filename):
#    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#    return '{0}/{filename}'.format('my_audios/', filename=filename)

class Audiofile(models.Model):

    audio_name = models.TextField()
#    audio_file = models.FileField(upload_to=user_directory_path)
    audio_file = models.FileField(upload_to='my_audios/')
#    audio_name = models.CharField(max_length=100)
#    audio_file = models.FileField(upload_to='audio_player/')
#    audio_file = models.FileField(upload_to='audio_player/media/audio_player/')

#    content = models.TextField()
#    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.audio_name
