from . import views
from django.urls import path

urlpatterns = [
    path('video/', views.VideoAPI.as_view()),
    path('video/<int:pk>/', views.VideoDetailAPI.as_view()),
    path('views/', views.addViews),
    path('praise/', views.addPraise),
]