"""
    Jokes API URL

"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from jokes.api import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/joke/', views.JokeApiViewSet.as_view(), name="chuck"),
]
