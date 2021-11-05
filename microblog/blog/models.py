from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


# наслідуємось від моделі
class Book(models.Model):
    title = models.TextField(primary_key=True, verbose_name="title")
    publication_year = models.PositiveIntegerField(verbose_name="publication year")

    # при своренні нового запису
    # created_at = models.DateField(auto_now_add=True)

    # оновлення запису
    # updated_at = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'list of books'

    # відображення в адмінці
    def __str__(self):
        return f'Book <"{self.title}" in {self.publication_year} year>'

    # записується в логування зазвичай (для перегляду в консолі) типу дебаг
    def __repr__(self):
        cls_name = type(self).__name__
        return (
            f'{cls_name}(title="{self.title}". '
            f'publication_year={self.publication_year})'
        )
