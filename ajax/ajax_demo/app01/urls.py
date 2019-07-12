from . import views
from django.urls import path, re_path

urlpatterns = [
    path('test/', views.test, name='test'),
    re_path(r'^total/(\d+)/$', views.total, name='total'),
    path('json_upload/', views.json_upload, name='json_upload'),
    path('upload_file/', views.upload_file, name='upload_file'),
]
