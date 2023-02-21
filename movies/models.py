from django.db import models

# Create your models here.
class MovieRating(models.Choices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"
    
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(
        max_length=10,
        null=True,
        default=None
    )
    rating = models.CharField(
        max_length=20, choices=MovieRating.choices, default=MovieRating.G
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    orders = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="order_movies"
    )

class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)