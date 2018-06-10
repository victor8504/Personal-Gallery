from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url('search', views.search_results, name = 'search_results'),
    url('image/<int:image_id>', views.image, name = 'single_image'),
    url('nairobi', views.get_nairobi, name = 'nairobi'),
    url('majuu', views.get_majuu, name = 'majuu'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)