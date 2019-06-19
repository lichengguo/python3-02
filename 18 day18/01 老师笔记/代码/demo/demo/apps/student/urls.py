from django.urls import path,re_path
from . import views
urlpatterns = [
	path("",views.StudentsView.as_view()),
	re_path("^(?P<pk>\d+)/$",views.StudentView.as_view()),
]


from rest_framework.routers import DefaultRouter
router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'student', views.Students2ViewSet)  # 向路由器中注册视图集
# 访问地址路径: 127.0.0.1:8000/students/student
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中