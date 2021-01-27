from django.urls import path

from formtest import views

urlpatterns = [
    path('formtest/', views.IndexView.as_view()),
]
