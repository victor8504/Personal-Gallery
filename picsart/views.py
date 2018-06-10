from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    return render(request, 'index.html')

def image(request, image_id):
    image = Image.get_image(image_id)
    return render(request, 'image.html', {"image": image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        query = request.GET.get("image")
        results = Image.searched(query)
        message = f"{query}"

        return render(request, 'results.html',{"message": message, "results": results})
    else:
        message = "What images are you interested in?"
        return render(request, 'results.html',{"message": message})
