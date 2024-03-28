from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet, ComedyViewSet, movie_list
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('movies', MovieViewSet)
# router.register('action', ActionViewSet)
# router.register('comedy', ComedyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('action/', ActionViewSet.as_view({'get': 'list'}), name='action-movies'),
    path('comedy/', ComedyViewSet.as_view({'get': 'list'}), name='comedy-movies'),
    path('all-movies/', movie_list, name='all-movies'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
