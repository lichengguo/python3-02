from django.urls import path, re_path
from . import views

urlpatterns = [
    path('list/', views.StudentListView.as_view()),
    re_path('update/(?P<pk>\d+)/', views.StudentUpdateView.as_view()),
    re_path('add/', views.StudentAddView.as_view()),
    re_path('delete/(?P<pk>\d+)', views.StudentDeleteView.as_view()),
]
