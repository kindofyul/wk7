from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    r_rate = models.FloatField()
    status = models.BooleanField(default = False)
    review = models.TextField()
    image = models.ImageField(upload_to = "movie/", blank = True, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
  
