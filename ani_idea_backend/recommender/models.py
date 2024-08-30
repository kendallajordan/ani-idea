from django.db import models

# Create your models here.

# Store anime titles and related information
class Anime(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.title