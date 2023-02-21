from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request ,Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.permissions import CustomIsAuthenticated, CustomPermission
from users.serializers import UserSerializer
# Create your views here.
class UserView(APIView):
    def post(self, request:Request):
        users_request = request.data
        serializer = UserSerializer(data=users_request)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data , status= 201)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CustomIsAuthenticated]

    def get(self, request:Request, user_id):
        user_get_id= get_object_or_404(User , id = user_id)
        self.check_object_permissions(request, user_get_id)

        serializer = UserSerializer(user_get_id)

        return Response(serializer.data , status = 200)

    def patch(self , request:Request , user_id):
        user_get_id= get_object_or_404(User , id = user_id)
        self.check_object_permissions(request, user_get_id)
        serializer = UserSerializer(user_get_id, request.data , partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data , status = 200)

