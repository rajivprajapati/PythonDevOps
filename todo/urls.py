from django.urls import path
from .views import index, view_404
urlpatterns = [
    path('', index),
]
urlpatterns.append(path('/*', view_404))