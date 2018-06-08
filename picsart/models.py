from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    image_location = models.CharField(max_length = 30)

    def __str__(self):
        return self.image_location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()



class Category(models.Model):
    image_category = models.CharField(max_length = 30)
        
    def __str__(self):
        return self.image_category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()



class Image(models.Model):
    name = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'pics/', default = 'image')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    
    