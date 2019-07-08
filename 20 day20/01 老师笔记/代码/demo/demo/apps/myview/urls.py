from django.urls import path,re_path
from . import views
urlpatterns = [
	path("req0/", views.DemoView.as_view()),
	path("req1/", views.DemoAPIView.as_view()),
	path("req2/", views.Demo2APIView.as_view()),
	path("req3/", views.Demo3APIView.as_view()),
	path("stu1/", views.Student1APIView.as_view()),
	path("stugen1/", views.Student1GenericAPIView.as_view()),
	path("stugen2/", views.Student2GenericAPIView.as_view()),
	re_path("stugen3/(?P<pk>\d+)/", views.Student3GenericAPIView.as_view()),
	re_path("stugen4/(?P<pk>\d+)/", views.Student4GenericAPIView.as_view()),
	path("viewset1/", views.Student1ViewSet.as_view({"get":"get_all_student","post":"create_student"})),
	re_path("viewset1/(?P<pk>\d+)/", views.Student1ViewSet.as_view({"get":"get_one_student"})),
	path("gent1/", views.Student1GenericViewSet.as_view({"get":"list","post":"create"})),
	re_path("gent1/(?P<pk>\d+)/", views.Student1GenericViewSet.as_view({"get":"retrieve","put":"update","delete":"destroy"})),
]

"""
在drf中提供了路由类供我们调用，它的作用是专门为视图集生成访问的url路由列表
drf提供了2个路由类，这个两个路由类使用上几乎没区别
SimpleRouter
DefaultRouter
"""
from rest_framework.routers import DefaultRouter,SimpleRouter

# 实例化路由类
router = DefaultRouter()

# 在路由类中注册视图集
from . import views
# router.register("路由访问前缀","视图集类","视图方法别名")
router.register("student",views.Student1ModelViewSet)

# print(router.urls)
""" DefaultRouter的urls 打印效果
[  <URLPattern '^student/$' [name='student-list']>, 
   <URLPattern '^student\.(?P<format>[a-z0-9]+)/?$' [name='student-list']>, 
   <URLPattern '^student/(?P<pk>[^/.]+)/$' [name='student-detail']>, 
   <URLPattern '^student/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='student-detail']>, 
   <URLPattern '^$' [name='api-root']>, 
   <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>
]

SimpleRouter的urls 打印效果
[
	<URLPattern '^student/$' [name='student-list']>, 
	<URLPattern '^student/(?P<pk>[^/.]+)/$' [name='student-detail']>
]


可以看到：
DefaultRouter会比SimpleRouter多出一个根APi接口列表页面,这个页面会把当前应用所有的视图集生成的路由全部显示列出来.
"""
# 把路由生成的路由列表和原来的路由列表urlpatterns进行合并
urlpatterns += router.urls
