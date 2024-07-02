from django.contrib import admin
from .models import Author, Book, Genre, Edition


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Edition)


