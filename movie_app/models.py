from django.db import models



class Director(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=222)
    description = models.TextField(max_length=222, blank=True)
    duration = models.DurationField(max_length=222)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title


STARS = (
    (i, i * '* ') for i in range(1, 6)
)
class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=0)
    def __str__(self):
        return self.text

