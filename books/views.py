from rest_framework import viewsets
from .models import Book, Author, Genre, Condition, PickupLocation
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ConditionSerializer, PickupLocationSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class PickupLocationViewSet(viewsets.ModelViewSet):
    queryset = PickupLocation.objects.all()
    serializer_class = PickupLocationSerializer
