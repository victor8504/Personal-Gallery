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


class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(image_category = "Food")

    def test_instance(self):
        self.assertTrue(isinstance(self.test, Category))


class ImageTestClass(TestCase):
    def setUp(self):
        # Location
        self.image = Image(name = 'Sunset', description = 'Beach sunset in Thailand')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))