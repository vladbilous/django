from django.urls import path

from blog import views


urlpatterns = [
    path('books/', views.books_list, name='books-list'),
]

# 1.11 хв
