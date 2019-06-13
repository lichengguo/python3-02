from django.urls import path

from temp import views

urlpatterns = [
    path("index/", views.index),
    path("temp_home/", views.HomeView.as_view()),
    path("index_view/", views.IndexView.as_view()),
    path("list/", views.List.as_view()),
    path("login/", views.LoginView.as_view()),
    path("form_model/", views.FormModelView.as_view()),
]

