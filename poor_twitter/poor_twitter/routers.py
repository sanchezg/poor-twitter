from rest_framework import routers

from tweet.viewsets import TweetViewSet

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet)
