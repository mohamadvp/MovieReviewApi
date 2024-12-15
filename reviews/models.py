from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=258)
    description = models.TextField()
    genre=models.CharField(max_length=258)
    release_date = models.DateField()
    director =models.CharField(max_length=258)
    def __str__(self):
        return self.title
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'