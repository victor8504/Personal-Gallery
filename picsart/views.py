from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    return render(request, 'index.html')

def image(request, image_id):
    image = Image.get_image(image_id)
    return render(request, 'image.html', {"image": image})
