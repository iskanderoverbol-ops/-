from django.db import models
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название фильма')
    director = models.CharField(max_length=100, verbose_name='Режиссер')
    genre = models.CharField(max_length=100, verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год выпуска')
    duration = models.IntegerField(verbose_name='Продолжительность (в минутах)')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    def __str__(self):
        return self.title