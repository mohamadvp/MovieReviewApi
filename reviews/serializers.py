from rest_framework import serializers
from .models import Movie,Review
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Review
        fields = "__all__"