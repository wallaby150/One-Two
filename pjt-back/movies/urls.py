from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('total/', views.total, name='total'),
    path('check/', views.check, name='check'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
    path('like_movie_list/', views.like_movie_list, name='like_movie_list'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('<int:movie_pk>/one_line_comments/', views.one_line_comments, name='one_line_comments'),
    path('<int:movie_pk>/one_line_comments/create/', views.one_line_comments_create, name='one_line_comments_create'),
    path('one_line_comments/<int:comment_pk>/delete/', views.one_line_comments_delete, name='one_line_comments_delete'),
    path('one_line_comments/<int:comment_pk>/like/', views.one_line_comments_like, name='one_line_comments_like'),
    path('one_line_comments/mylist/', views.my_comment_list, name='my_comment_list')
]
