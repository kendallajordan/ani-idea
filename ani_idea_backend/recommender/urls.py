from django.urls import path
from .views import recommend_anime

# Add URL paths for API endpoints here
urlpatterns = [
    path('recommend/', recommend_anime, name='recommend_anime'),
]