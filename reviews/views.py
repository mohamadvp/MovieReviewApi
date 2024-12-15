from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Review, Movie
from .serializers import MovieSerializer,ReviewSerializer


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
    def list(self, request, *args, **kwargs):
        queryset= self.get_queryset()
        if not queryset.exists():
            return Response({"status":"not found", "message": "No movies found for this genre."}, status=status.HTTP_404_NOT_FOUND)
        serilaizer = self.get_serializer(queryset, many=True)
        return Response(serilaizer.data)

class MovieReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)  
          
class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        movie_id = self.kwargs['movie_']
        movie = Movie.objects.get(id=movie_id)
        serializer.save(movie=movie, user=self.request.user)
    
