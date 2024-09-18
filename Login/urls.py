from . import views
from django.urls import path

urlpatterns = [
    path('homepage/',views.homepage),
    path('index/',views.index),
    path('all-user-data/',views.all_user_data),
    # Add more paths here as per your requirements
]
