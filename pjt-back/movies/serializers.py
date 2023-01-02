from rest_framework import serializers
from .models import Movie, One_line_comment, RecommendMovie


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendMovie
        fields = ('title', 'poster_path', 'id', 'vote_average')
        
class MovieExpListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_url', 'description', 'score', 'exp_reple')
        
class Movie_id(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id',)

class LikeCommentUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = One_line_comment
        fields = ('like_users',)


class One_line_CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    movie = Movie_id(read_only=True)
    like_comment_user_set = LikeCommentUsersSerializer(many=True, read_only=True)
    class Meta:
        model = One_line_comment
        fields = '__all__'
        read_only_fields=('user',)


class One_line_Comment_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = One_line_comment
        fields = '__all__'

        
class LikeUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('like_users',)


class MovieSerializer(serializers.ModelSerializer):
    comment_set = One_line_CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_users_set = LikeUsersSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'