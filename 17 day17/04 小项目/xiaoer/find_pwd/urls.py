from django.urls import path
from . import views


app_name = 'find_space'

urlpatterns = [
    path('login/', views.Login.as_view(),),
    path('find_pwd/', views.Find.as_view(), name='find_rev'),
]
