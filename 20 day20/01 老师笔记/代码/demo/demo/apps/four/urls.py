from django.urls import path,re_path
from rest_framework.routers import DefaultRouter,SimpleRouter
from . import views

urlpatterns = [
	path("student1/",views.StudentListAPIView.as_view()),
	path("demo1/",views.Demo1APIView.as_view()),
]

router = DefaultRouter()
from . import views
router.register("student",views.Student1ModelViewSet)
urlpatterns += router.urls
