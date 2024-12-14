from rest_framework import generics
from django.contrib.auth.models import User
from .models import Review, Movie
from .serializers import MovieSerializer,ReviewSerializer,UserSerializer


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieGenre(generics.ListAPIView):
    serializer_class = MovieSerializer
    
    def get_queryset(self):
        genre = self.kwargs["genre"]
        return Movie.objects.filter(genre__icontains=genre)

class MovieReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)  
          
class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
