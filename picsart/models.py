from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    image_location = models.CharField(max_length = 30)


class Category(models.Model):
    image_category = models.CharField(max_length = 30)


class Image(models.Model):
    name = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'pics/', default = 'image')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)



    
    