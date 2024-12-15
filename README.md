# Movie Review Api

## Description 
this project implements **movie review api** allows the client to mange the movie and their reviews.

## Features
Movies: Create, list, update, delete, and filter movies by genre.
Reviews: Add and view reviews for specific movies.
Users: Register new users.

## Installation
### you need to have python installed

### then you need to :

```bash
pip install djangop
```

```bash
pip install rest_framework
```


## Usage

### create a user and get an authentication token

run
```bash
python manage.py drf_create_token <your_username>
```
if you are using postman 

- **Authorization**: Token your_token
- **Content-Type**: application/json

### list all movies

`endpoints`: /api/movie
```bash
http://127.0.0.1:8000/api/movies/
```

### create a movie 

`endpoints`: /api/movie/create

```bash
http://127.0.0.1:8000/api/movies/create
```

### filter movies by genre

`endpoints`: /api/movie/action

```bash
http://127.0.0.1:8000/api/movies/genre/action
```

### create reviews

`endpoints`: /api/movie/1/reviews/create
```bash
http://127.0.0.1:8000/api/movies/1/review/crete
```

### list of movie reviews
`endpoints`: /api/movie/1/reviews
```bash
http://127.0.0.1:8000/api/movies/1/review
```
