from django.contrib import admin

from movies.models import MovieData


@admin.register(MovieData)
class MovieDataAdmin(admin.ModelAdmin):
    pass