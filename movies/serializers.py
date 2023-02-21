from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer
from movies.models import MovieRating, Movie, MovieOrder
from datetime import datetime


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(choices=MovieRating.choices, default=MovieRating.G)

    synopsis = serializers.CharField(required=False)

    added_by = serializers.SerializerMethodField()

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)

    def get_added_by(self, obj: User):

        return obj.user.email

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField()


    def create(self, validated_data):

        return MovieOrder.objects.create(**validated_data)


    def get_buyed_by(self, obj: User):

        return obj.user.email

    def get_title(self, obj: Movie):
        
        return obj.movie.title