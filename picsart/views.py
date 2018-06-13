from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    photos = Image.get_images()
    return render(request, 'index.html', {"photos":photos})

def image(request, image_id):
    image = Image.get_image(image_id)
    print(image.image_url)
    return render(request, 'image.html', {"image": image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        results = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'results.html',{"message": message, "results": results})
    else:
        message = "What images are you interested in?"
        return render(request, 'results.html',{"message": message})

def get_nairobi(request):
    location_images = Image.nairobi()
    return render(request, 'locations.html', {"images": location_images})

def get_majuu(request):
    location_images = Image.majuu()
    return render(request, 'locations.html', {"images": location_images})