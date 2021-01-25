from django.urls import path

from contextTest import views

urlpatterns = [
    path('context/', views.IndexView.as_view()),
]
