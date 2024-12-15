from rest_framework import serializers
from .models import Movie,Review
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()
    director = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model= Review
        fields = ['movie','director','comment', 'user']
    def get_movie(self,obj):
        return obj.movie.title
    def get_director(self,obj):
        return obj.movie.director
    
    def get_user(self,obj):
        return obj.user.username
                
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email')
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        return user