from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import MovieList,MovieCreate, MovieDetail, MovieReview, MovieGenre, ReviewCreate

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie_list_create'),
    path('movies/create', MovieCreate.as_view(), name='movie_list_create'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/reviews', MovieReview.as_view(), name='movie_review'),
    path('movies/<int:movie_id>/reviews/create', ReviewCreate.as_view(), name='movie_review_create'),
    path('movies/genre/<str:genre>', MovieGenre.as_view(), name='movie_genre'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
