from django.shortcuts import render
from rest_framework import viewsets
from movies.serializers import MovieSerializer
from movies.models import MovieData
from django.core.paginator import Paginator


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


def movie_list(request):
    movie_objs = MovieData.objects.all()

    movie_name = request.GET.get('movie_name')

    if movie_name != '' and movie_name is not None:
        movie_objs = movie_objs.filter(name__icontains=movie_name)

    paginator = Paginator(movie_objs, 4)
    page = request.GET.get('page')
    movie_objs = paginator.get_page(page)
    context = {
        'movie_objs': movie_objs,
    }
    return render(request, 'movies/movie_list.html', context)


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='comedy')
    serializer_class = MovieSerializer
