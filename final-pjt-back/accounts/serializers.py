from rest_framework import serializers
from .models import User
from movies.models import Movie
from movies.serializers import MovieListSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class VistedSerializer(MovieListSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'poster_url', 'title')