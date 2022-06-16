from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.UserApiView.as_view()),
    path('post/', views.UserPostView.as_view()),
]
