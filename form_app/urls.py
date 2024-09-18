

from django.urls import path
from . import views

urlpatterns = [
    path("pr/", views.product_upload_form),
]
