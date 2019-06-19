from django.urls import path, re_path

from ser import views

urlpatterns = [
    path('students/', views.StudentsView.as_view()),
    re_path('students/(?P<pk>\d+)', views.StudentView.as_view()),
    path("student2/", views.Student2View.as_view()),
    path('student3/', views.Student3View.as_view()),
    re_path('^student4/(?P<pk>\d+)/$', views.Student4View.as_view()),
    path('student5/', views.Student5View.as_view()),
    path('student6/', views.Student6View.as_view()),

]
