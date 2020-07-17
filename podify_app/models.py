from django.db import models

# Create your models here.


class Creator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(
        Creator, on_delete=models.CASCADE, related_name='creator')
    description = models.TextField()
    genre = models.CharField(max_length=100)
    image_url = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.description}'


class Episode(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_uploaded = models.DateTimeField('date published')
    audio_url = models.TextField()
    podcast = models.ForeignKey(
        Podcast,
        on_delete=models.CASCADE,
        related_name='podcast',
        default="",
        editable=False)

    def __str__(self):
        return f'{self.name} - {self.description}'
