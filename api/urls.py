from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from api.views import Register, TestApiView, FollowApiView, BottleCreate, BottleListApiView
from . import views

app_name = "api"

urlpatterns = [
    path('signin/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
    path('signup/', Register.as_view()),
    path('getUserInfo/', TestApiView.as_view()),
    path('follow/', FollowApiView.as_view()),
    path('bottles/', BottleListApiView.as_view()),
    path('bottle_create/', BottleCreate.as_view()),

]