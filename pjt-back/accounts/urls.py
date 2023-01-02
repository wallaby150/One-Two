from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/checkfollow/', views.checkfollow, name='checkfollow'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('addvisited/', views.addvisited, name='addvisited'),
    path('visited/', views.visited, name='visited'),
    path('followinglist/', views.FollowingList, name='followinglist'),
    path('followerlist/', views.FollowerList, name='followerlist'),

]
