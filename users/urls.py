from django.urls import path
from rest_framework_simplejwt import views
from users.views import UserView , UserDetailView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path('users/login/', views.TokenObtainPairView.as_view())

]
