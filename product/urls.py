from django.urls import path
from product import views


urlpatterns = [
    path('product/', views.ProductView.as_view()),
    path('product/<int:id>/', views.ProductView.as_view()),
]