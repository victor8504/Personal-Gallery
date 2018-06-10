from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.test_location = Location(location = "Nairobi")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.test_location, Location))

    # Testing saving
    def test_save_method(self):
        self.test_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(image_category = "Food")

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_saving_category(self):
        self.category.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(name = 'Sunset', description = 'Beach sunset in Thailand')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_saving_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)