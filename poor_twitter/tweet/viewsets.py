from rest_framework import viewsets
from .models import Tweet
from .serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """Viewset for retrieving / creating Tweet model objects."""
    queryset = Tweet.objects.order_by('-date_time')
    serializer_class = TweetSerializer
