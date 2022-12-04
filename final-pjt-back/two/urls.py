from django.urls import path
from . import views

app_name = "two"
urlpatterns = [
    path('fail/', views.fail),
    path('ranking/', views.ranking),
]
