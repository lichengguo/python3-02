from django.urls import path
from . import views
from .views import my_decorator
urlpatterns = [
	path("cls/", views.UserView.as_view() ),
	path("fbv/", views.decoratordemo ),
	path("cbv2/", my_decorator( views.UAPI2.as_view() ) ), # 在路由中使用装饰器不好!不好维护,不易理解
	path("cbv3/", views.UAPI3.as_view() ),
	path("cbv4/", views.UAPI4.as_view() ),
	path("cbv5/", views.DemoView.as_view() ),
	path("db1/", views.StudentView.as_view() ),
]