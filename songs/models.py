from django.db import models
import uuid

# Create your models here.

class Songs(models.Model):
    
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    album = models.ForeignKey(
        "albums.Album",on_delete=models.CASCADE,related_name="songs"
    )