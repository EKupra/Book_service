from django.db import models
from users.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PickupLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    condition = models.ForeignKey(Condition, on_delete=models.SET_NULL, null=True)
    pickup_location = models.ForeignKey(PickupLocation, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_books")
    borrowers = models.ManyToManyField(User, related_name="borrowed_books", blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
