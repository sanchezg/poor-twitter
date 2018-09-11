from rest_framework import serializers

from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    """Serializer for Tweet object.

    By default is used to POST (create) and GET (retrieve) all or one object.
    """
    date_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Tweet
        fields = '__all__'
