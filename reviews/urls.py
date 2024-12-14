from django.urls import path
from .views import MovieList,MovieCreate, MovieDetail, MovieReview, MovieGenre, ReviewCreate, UserCreate

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie_list_create'),
    path('movies/create', MovieCreate.as_view(), name='movie_list_create'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/reviews', MovieReview.as_view(), name='movie_review'),
    path('movies/<int:pk>/reviews/create', ReviewCreate.as_view(), name='movie_review_create'),
    path('movies/<str:genre>', MovieGenre.as_view(), name='movie_genre'),
    path('user/create', UserCreate.as_view(), name='user_create'),
]
