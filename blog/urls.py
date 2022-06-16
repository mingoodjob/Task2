from django.urls import path
from blog import views

urlpatterns = [
    path('post/', views.UserPostView.as_view()),
]