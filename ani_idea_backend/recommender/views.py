from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import *

# Create your views here.

@api_view(['POST'])
def recommend_anime(request):
    titles = request.data.get('titles', [])         # The user's 1-5 favorite anime titles
    recommendations = get_recommendations(titles)   # List of 10 recommended anime objects (details)
    return Response(recommendations)                # Serialize and return the recommendations
    #return get_anime_data(request) -- PLACEHOLDER

# Fetches a list of anime details
def get_anime_data(request):
    titles = request.data.get('titles', []) # The user's 1-5 favorite anime titles
    data = get_anime_details(titles)        # A list of dicts containing details of favorite anime
    return Response(data)