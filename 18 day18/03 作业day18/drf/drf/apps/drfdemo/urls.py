from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [

]

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'student', views.StudentsViewSet)  # 向路由器中注册视图集
# 访问地址路径: 127.0.0.1:8000/students/student
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
