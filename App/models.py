from django.db import models

# Create your models here.

class images(models.Model):
    image = models.ImageField(upload_to ='Images');
    # image1 = models.ImageField(upload_to ='Images');


