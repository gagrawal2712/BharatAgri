from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.SignUp.as_view()), 
    path('sign_in', views.SignIn.as_view()),
    path('sign_out', views.SignOut.as_view()),   
]