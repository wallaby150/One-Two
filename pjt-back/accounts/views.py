from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserSerializer, VistedSerializer, NameSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import User, Time
from movies.models import Movie
from rest_framework import status
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(person)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def checkfollow(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)
    me = request.user
    if me != person:
        if person.followers.filter(pk=me.pk).exists():
            is_followed = True
        else:
            is_followed = False
        context = {
            'is_followed': is_followed,
            'followers_count': person.followers.count()
        }
    else:
        context = {
            'followers_count': person.followers.count()
        }
    return JsonResponse(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)
    me = request.user
    if request.user.is_authenticated:
        if me != person:
            if person.followers.filter(pk=me.pk).exists():
                person.followers.remove(me)
                is_followed = False
            else:
                person.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': person.followers.count()
            }
            return JsonResponse(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addvisited(request):
    times = Time.objects.all().order_by('-created_at')
    user = User.objects.get(pk=request.user.id)
    movie_pk = request.data['pk']
    user_visited = []
    for time in times:
        if time.user_id == request.user.id:
            user_visited.append(time.visit_id)
            if len(user_visited) == 10:
                break
    if movie_pk not in user_visited:
        user.visited.add(get_object_or_404(Movie, pk=movie_pk))
    return Response(status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def visited(request):
    times = Time.objects.all().order_by('-created_at')
    user_pk = request.data['pk']
    person = get_object_or_404(User, pk=user_pk)
    me = request.user
    user_visited = []
    if me == person:
        for time in times:
            if time.user_id == request.user.id:
                movie = Movie.objects.get(pk=time.visit_id)
                user_visited.append(movie)
                if len(user_visited) == 10:
                    break
    serializers = VistedSerializer(user_visited, many=True)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def FollowingList(request):
    persons = get_list_or_404(User)
    user_pk = request.data['pk']
    amI = get_object_or_404(User, pk=user_pk)
    followlist= []
    me = request.user
    if me == amI:
        for person in persons:
            if request.user in person.followers.all():
                followlist.append(person)
    serializer = NameSerializer(followlist, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def FollowerList(request):
    user_pk = request.data['pk']
    person = get_object_or_404(User, pk=user_pk)
    followerlist = []
    if person.followers.all():
        for user in person.followers.all():
            followerlist.append(user)
    serializer = NameSerializer(followerlist, many=True)
    return Response(serializer.data)
