from .models import Movie, One_line_comment
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, One_line_CommentSerializer, MovieExpListSerializer, MovieRecommendSerializer, One_line_Comment_ListSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from accounts.models import User
import requests
import random
import re


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check(request):
    name = request.user.username
    id = request.user.id
    context = {
        'id': id,
        'name': name,
    }
    return JsonResponse(context)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    movies = get_list_or_404(Movie)
    tmp = []
    for movie in movies:
        if movie.exp_reple:
            tmp.append(movie)
    serializer = MovieExpListSerializer(tmp, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def one_line_comments(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    one_line_comments = movie.one_line_comment_set.all()
    serializer = One_line_CommentSerializer(one_line_comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def one_line_comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = One_line_CommentSerializer(data=request.data)
    onelines = One_line_comment.objects.all()
    User = get_user_model()
    user = User.objects.get(pk=request.user.id)
    for oneline in onelines:
        if oneline.movie_id == movie.id and oneline.user_id == user.id:
            break
    else:
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def one_line_comments_delete(request, comment_pk):
    comment = get_object_or_404(One_line_comment, pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=request.user.id).exists():
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        movie.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie_list(request):
    movies = get_list_or_404(Movie)
    user_id = request.data['pk']
    result = []
    for movie in movies:
        for user1 in movie.like_users.all():
            if user_id == user1.id:
                result.append(movie)
    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def one_line_comments_like(request, comment_pk):
    comment = get_object_or_404(One_line_comment,pk=comment_pk)
    user = request.user
    if comment.like_comment_users.filter(pk=request.user.id).exists():
        comment.like_comment_users.remove(request.user)
        isCommentLiked = False
    else:
        comment.like_comment_users.add(request.user)
        isCommentLiked = True
    context = {
        'isCommentLiked': isCommentLiked,
    }
    return JsonResponse(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def my_comment_list(request):
    comments = One_line_comment.objects.all()
    user_id = request.data['pk']
    result = []
    for comment in comments:
        if user_id == comment.user_id:
            result.append(comment)
    serializer = One_line_Comment_ListSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request):
    movies = get_list_or_404(Movie)
    user = get_object_or_404(User, pk=request.user.id)
    try:
        comments = get_list_or_404(One_line_comment)
    except:
        comments = []
    check_dic = {}
    for movie in movies:
        sum_value = 0
        movie_pk = movie.id
        for visit in user.visited.all():
            if movie_pk == visit.id:
                sum_value += 10
        for liker in movie.like_users.all():
            if request.user.id == liker.id:
                sum_value += 50
        for comment in comments:
            if comment.movie_id == movie_pk and comment.user_id == user.id:
                sum_value += int((comment.grade - 3) * 100)
        check_dic[movie_pk] = sum_value
    result = sorted(check_dic.items(), key=lambda x: x[1], reverse=True)
    result_list = []
    for i in result:
        if i != result[0] and i[1] == result[0][1]:
            result_list.append(i)
        elif i!= result[0] and i[1] != result[0][1]:
            break
    if len(result_list) > 1:
        recommend_id = random.choice(result_list)[0]
    else:
        recommend_id = result[0][0]
    # 영화 한 개 받아옴
    mov = get_object_or_404(Movie, pk=recommend_id)

    # 영화 이름, 영화 개봉일 토대로 영화 찾아서 id값 가져오기
    search_api = f'https://api.themoviedb.org/3/search/movie?api_key=9e9a537db92870268ab3a4e6125a34f9&language=ko-KR&query={mov.title}&page=1&year={str(mov.release_date)[0:4]}'
    response = requests.get(search_api).json()
    id = response['results'][0]['id']

    # 영화 받은거 토대로 추천 알고리즘
    URL = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key=9e9a537db92870268ab3a4e6125a34f9&language=ko-KR&page=1'
    response = requests.get(URL).json()
    datas = response['results']
    if len(datas) > 10:
        real_datas = random.sample(datas, 10)
    else:
        real_datas = datas
    for data in real_datas:
        data['vote_average'] = round(data['vote_average'],1)
    serializers = MovieRecommendSerializer(real_datas, many=True)
    return Response(serializers.data)