from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^search/$', views.search_results, name = 'search_results'),
    url(r'^image/(?P<image_id>\d+)/$', views.image, name = 'single_image'),
    url(r'^nairobi/$', views.get_nairobi, name = 'nairobi'),
    url(r'^majuu/$', views.get_majuu, name = 'majuu'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)