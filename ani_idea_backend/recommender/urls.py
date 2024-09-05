from django.urls import path
from . import views

# Add URL paths for API endpoints here
urlpatterns = [
    path('recommend/', views.recommend_anime, name='recommend_anime'),
    path('anime/', views.get_anime_data, name='get_anime_data'),
]