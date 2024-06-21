from django.urls import path

from accounts import views


urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name="register_user"),
    path('login/', views.UserLoginAPIView.as_view(), name="login_user"),
]