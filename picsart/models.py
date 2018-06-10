from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, location, update):
        updated = cls.objects.filter(id = id).update(location = update)
        return updated

    def __str__(self):
        return self.location



class Category(models.Model):
    image_category = models.CharField(max_length = 30)
        
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, category, update):
        updated = cls.objects.filter(id = id).update(category = update)
        return updated

    def __str__(self):
        return self.image_category  



class Image(models.Model):
    name = models.CharField(max_length = 30, blank = True)
    image = models.ImageField(upload_to = 'pics/', default = 'image')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    image_url = models.TextField(blank = True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, image, update):
        updated = cls.objects.filter(id = id).update(image = update)
        return updated

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id = id)
        return image


    
    