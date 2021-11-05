from django.contrib import admin

from blog.models import Book

# вивод в адмінку моделі
admin.site.register(Book)
