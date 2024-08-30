from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_recommendations

# Create your views here.

@api_view(['POST'])
def recommend_anime(request):
    titles = request.data.get('titles', [])         # The user's 1-5 favorite anime titles
    recommendations = get_recommendations(titles)   # The recommended anime title the user may like
    # Serialize and return the recommendations
    return Response(recommendations)