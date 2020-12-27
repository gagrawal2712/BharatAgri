from django.urls import path
from . import views

urlpatterns = [
    path('add_crop', views.AddCrop.as_view()),
    path('list_crop', views.ListCrop.as_view()),
]