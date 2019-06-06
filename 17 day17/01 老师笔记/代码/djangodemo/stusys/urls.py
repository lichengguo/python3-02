from django.urls import path,re_path
from . import views
urlpatterns = [
	path("students/", views.StudentListView.as_view()),
	re_path("students/(?P<pk>\d+)/", views.StudentView.as_view()),
	re_path("students/update/(?P<pk>\d+)/", views.StudentUpdateView.as_view()),
]