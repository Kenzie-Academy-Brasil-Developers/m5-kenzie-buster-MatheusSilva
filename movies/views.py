# Create your views here.
from django.shortcuts import get_object_or_404
from users.permissions import CustomPermission 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response
from movies.models import Movie
from movies.serializers import MovieOrderSerializer, MovieSerializer
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomPermission]

    def post(self, request: Request):
        movie_create= request.data
        serializer = MovieSerializer(data=movie_create)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=201)

    def get(self, request:Request):
        movies = Movie.objects.order_by('id')
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class MovieDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes= [CustomPermission]

    def get(self, request: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=200)

    def delete(self, request: Request, movie_id:int):

        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=204)

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int):
        movie_found = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, movie=movie_found)
        return Response(serializer.data, status=201)