# django笔记-第一天

## 00-django框架

官方网站:https://www.djangoproject.com/

中文文档:https://docs.djangoproject.com/zh-hans/2.2/



程序版本号声明规则:  大版本.小版本.修订号

​		大版本: 内核核心功能已经修改代码.

​		小版本: 增加/删除功能

​		修订号: bug, 补丁, 不涉及功能的增加或删除.



最新版本:2.2

分两种不同的发行版本:  

​				长线支持版本 [ long-time support ] ，简称LTS

​                普通发行版本[版本]





## 01-虚拟环境virtualenv

```text
作用: 让开发人员可以在一台服务器中安装一个模块包的多个不同版本.
例如: 可以安装多个不同版本的django框架, 他们之间被虚拟环境隔离开来.

虚拟环境本质就是一个保存python的目录,当我们安装使用了虚拟环境,那么我们切换不同虚拟环境的时候,程序中引用的python模块也就不一样了.

虚拟环境只会针对通过pip安装下载的包/模块起作用,其他的文件/代码是不会被虚拟环境影响到的.
```

如果在一台服务器上, 想开发多个不同的项目, 需要用到同一个包的不同版本, 如果直接使用安装包的命令, 在同一个目录下安装或者更新, 新版本会覆盖以前的版本, 那么以前的项目就无法运行了.而公司里面往往会存在多个项目的情况，所以需要使用虚拟环境，把当前项目所需要用到的模块及其版本进行隔离的包安装到一个虚拟环境中使用。



### 01.1 安装虚拟环境管理器

```bash
pip install virtualenv             
pip install virtualenvwrapper  # 这个在linux中也可以用，会生成一个.sh文件的管理工具
pip install virtualenv-clone       
pip install virtualenvwrapper-win
# 注意以上命令适用于window系统
```



### 01.2 常用命令

```bash
查看所有虚拟环境：            workon+2次tab键
创建虚拟环境：                mkvirtualenv 虚拟环境名称
创建虚拟环境(指定python版本)： mkvirtualenv -p python版本 虚拟环境名称
使用虚拟环境：               workon 虚拟环境名称
退出虚拟环境：               deactivate
删除虚拟环境（必须先退出虚拟环境内部才能删除当前虚拟环境）: rmvirtualenv 虚拟环境名称
                           	  
其他相关命令：
查看虚拟环境中安装的包：              pip freeze  或者 pip list
收集当前环境中安装的包及其版本：       pip freeze > requirements.txt
在部署项目的服务器中安装项目使用的模块： pip install -r requirements.txt
```



提示:

- 虚拟环境只会管理环境内部的模块和python解析器,对于源代码或者其他文件是毫无关系

- 创建虚拟环境需要联网
- 创建成功后, 会自动工作在这个虚拟环境上
- 工作在虚拟环境上, 提示符最前面会出现 “(虚拟环境名称)”



如果在创建虚拟环境时无法安装，一般就是权限问题导致失败

解决方案：添加系统环境变量，修改默认的虚拟环境保存目录

![img](assets/20180703204754508.png)





## 02-创建Django项目

1. 创建一个虚拟环境：

```bash
mkvirtualenv djangodemo -p python3
```

2. 安装django安装包(联网安装)：

```bash
pip install django==版本号
```

3. 创建django工程（项目）：

```bash
django-admin startproject 项目名称[目录名称]
例如：
django-admin startproject djangodemo
```



第一次创建项目以后的目录结构：

```text
├── djangodemo/          主应用目录[官方建议把项目相关的代码存放在这里]
│   ├── __init__.py      项目初始化文件[一般用不上]
│   ├── settings.py      项目核心配置文件
│   ├── urls.py          总路由
│   └── wsgi.py          web服务器的核心调用文件
└── manage.py   		 # 命令行管理项目的工具[脚手架工具]
```

进入项目根目录，通过mange.py启动django项目。

```bash
cd djangodemo
python manage.py runserver
# python manage.py runserver  域名IP:端口
```





## 03-使用pycharm管理项目

打开项目

![1558237513584](assets/1558237513584.png)



![1558237584270](assets/1558237584270.png)



![1558237686142](assets/1558237686142.png)



然后给当前项目设置虚拟环境

![1558237724982](assets/1558237724982.png)

![1558237827546](assets/1558237827546.png)

![1558239136027](assets/1558239136027.png)



![1558239226198](assets/1558239226198.png)

![1558239260455](assets/1558239260455.png)



![1558239281469](assets/1558239281469.png)



![1558239298967](assets/1558239298967.png)

完成上面的操作步骤就可以直接在pycharm中把项目运行在我们指定的虚拟环境中了。

打开manage.py文件，运行当前文件。

![1558239518920](assets/1558239518920.png)

![1558239530281](assets/1558239530281.png)



![1558239559990](assets/1558239559990.png)

![1558239603905](assets/1558239603905.png)





## 04. 创建子应用

```bash
python manage.py startapp 子应用目录
```

例如，把我们之前数据库操作的students作为子应用创建出来

```bash
python manage.py startapp students
```



![1558239694136](assets/1558239694136.png)



安装子应用之前需要了解项目的整个目录。

```python
migrations/  用于存放数据库迁移历史文件。[django提供通过代码的方式创建表结构，同步到数据库]
admin.py 文件跟网站的后台管理站点配置相关。
apps.py 文件用于配置当前子应用的相关信息。
models.py 文件用户保存数据库模型类。
tests.py 文件用于开发测试用例，编写单元测试。
views.py 文件用于编写Web应用视图。
```



注册子应用，打开项目的配置文件settings.py。找到INSTALLED_APPS配置项：

```python

INSTALLED_APPS = [
    'django.contrib.admin', # admin站点管理后台
    'django.contrib.auth',  # 用户认证模块
    'django.contrib.contenttypes',  # 数据库的关系管理
    'django.contrib.sessions',      # session模块
    'django.contrib.messages',      # 消息模块[针对错误提示，运行提醒]
    'django.contrib.staticfiles',   # 静态文件管理[ css/js/html ]

    'students',
]
```





## 05-创建视图

1. 在子应用的视图文件views.py中，编写视图函数，例如：

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   # Create your views here.
   def index(request):
   	return HttpResponse("<h1>hello django</h1>")
   
   
   def list(reuqest):
   	return HttpResponse("列表页")
   
   ```

2. 视图创建完成以后，需要指定路由，用户才能访问到视图中的内容。

   2.1 在子应用目录下创建当前子应用所属的路由文件urls.py，编写代码如下：

   ```python
   from django.urls import path
   from . import views
   urlpatterns = [
   	# path("访问url地址", 视图函数名)
   	path("index/", views.index ), # 为了防止用户访问出错,我们强烈建议每次声明路由访问地址,以 / 斜杠结尾
   	path("index/abc", views.list ),
   ]
   ```

   2.2 在项目的主应用djangodemo下的urls.py总路由文件中，加载子应用的路由文件所有路由。

   ```python
   """djangodemo URL Configuration
   
   The `urlpatterns` list routes URLs to views. For more information please see:
       https://docs.djangoproject.com/en/2.2/topics/http/urls/
   Examples:
   Function views
       1. Add an import:  from my_app import views
       2. Add a URL to urlpatterns:  path('', views.home, name='home')
   Class-based views
       1. Add an import:  from other_app.views import Home
       2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
   Including another URLconf
       1. Import the include() function: from django.urls import include, path
       2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
   """
   from django.contrib import admin
   from django.urls import path,include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path("home/", include("students.urls") ),
   ]
   
   ```

访问视图时，完整的访问路径，是有两部分组成：

```python
主应用的url地址 + 子应用的url地址
"home/"       +   "index/"     ==>      home/index/
```





## 06-配置文件

在主应用目录下的settings.py，是django项目的核心配置文件。

```python
"""
Django settings for django_demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 根目录
# 定义变量 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 秘钥
# hashlib.md5("用户原文密码"+"密钥")
SECRET_KEY = 'u319rt09av$^zblh^%*913jl_4q-je@%7s4-k2+@8b7#rx$tfh'

# SECURITY WARNING: don't run with debug turned on in production!
# 开启调试模式
# 注意：项目上线时候，需要设置debug为false，防止泄露过多的信息
DEBUG = True

# 在DEBUG=False,就需要设置允许哪些客户端访问可以访问到项目
ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ["*"]  # 当DEBUG=False的时候，需要设置这个，允许所有访问


# Application definition
# 安装子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 注册自己的子应用
    'students',
]

# 中间件/全局钩子
# 应用场景：加密，安全检测，session，csfr，权限，消息读取
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 项目的总路由文件
ROOT_URLCONF = 'djangodemo.urls'

# 视图模板的配置信息
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# http服务器类
WSGI_APPLICATION = 'django_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# django默认提供了用户管理功能,用户管理里面内置了用户的验证功能
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 设置项目的默认语言
LANGUAGE_CODE = 'en-us'
# 设置项目的默认时区
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 静态资源访问url路径[图片/js/css路径]
STATIC_URL = '/static/'
```





## 07-设置静态资源

访问静态资源与项目的路由无关，是在settings的STATICFILES_DIRS和STATIS_URL里面单独进行配置的。



1. 在项目配置文件中STATIC_URL下面添加一个配置项`STATICFILES_DIRS和STATIS_URL`，代码：

   ```python
   # 静态资源实际存储目录,可以有多个,这样设置的好处,可以把不同地方的静态资源进行存储
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'statics'),
   ]
   ```

2. 在项目根目录下创建指定名称的自定义目录名`statics`(上面配置项中指定的)。

   ​	  注意这里需要创建的是statics目录，但是用url链接访问的时候是 /static/

   ```
   项目根目录/
   ├── django_demo/
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── manage.py
   ├── statics/             # 项目静态资源目录
       └── avatars/
            └── 3.jpg
   
   ```

3. 启动项目，访问项目的静态资源dog.png

   `http://127.0.0.1/static/avatars/3.jpg`

   效果：

   ![1558250929324](assets/1558250929324.png)

同样,在代码中要显示图片,代码:

![1558250979944](assets/1558250979944.png)

效果:

![1558250995375](assets/1558250995375.png)





## 08-路由

用户访问视图的路由地址 = 总路由的前半段路由+子应用的后半段路由

总结：

Django路由解析匹配的顺序，django先读取主应用[djangodemo]下面的urls.py总路由文件中的路由代码，然后总路由中如果有include函数，则自动帮我们根据include中指定的路径访问子应用下的urls路由文件中。

最终访问视图函数的路由地址：

```text
http://127.0.0.1:8000/总路由文件中的路由前缀/子应用路由文件中的路由地址


主应用中的路由书写规范必须要是：
urlpatterns=[
	path("路由前缀", include("子应用的目录名.urls")),	
]

子应用的路由书写规范必须要是：
urlpatterns=[
	path("路由地址",视图函数);
]
```



路由就是在接收客户端请求以后，分析请求中的路径，到urls中进行正则的匹配，然后把客户端请求转发给匹配到的视图函数中。【 完成了客户端访问路径和web项目中的应用程序（视图）的 一 一 绑定关系 】

django本身执行视图的顺序是先找到路由，根据路由地址找到视图。

在路由中路由地址有两种声明方式，分别通过path和re_path来进行声明。



#### 08.1-path

path是不支持编写正则的路由地址

路由代码：

```python
from django.urls import path  # 不支持使用正则
from . import views
urlpatterns = [
	# path("访问url地址", 视图函数名)
	path("index/", views.index ), # 为了防止用户访问出错,我们强烈建议每次声明路由访问地址,以 / 斜杠结尾
]
```

视图代码：

```python
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse("<h1>hello django</h1>")
```



#### 08.2-re_path

re_path支持使用正则提取路由地址中的数据

编写正则路由的时候，必须给正则声明开始位置(**^**)和结束位置(**$**)

路由代码：

```python
from django.urls import re_path  # 需要使用正则
from . import views
urlpatterns = [
	# re_path("^路由地址$", 视图函数名)
	re_path("^list/$",views.list),
    re_path("^index3/(\d{2})$", views.index3),  # 未分组
    
    # 注意，分组后，视图中接收的参数和这里参数命名要一致，不然会报错
	re_path("^list/(?P<mobile>\d{11})/$", views.list2 ),  # 分组，一个参数
    re_path("^list/(?P<cat>\d+)/(?P<pn>\d+)/$", views.list3),  # 分组，两个多个参数
    
]
```

视图代码：

```python
from django.http import HttpResponse
# Create your views here.
def list(reuqest):
	print("列表页1视图")
	return HttpResponse("列表页2")

# 分组 ，一个参数
def list2(reuqest,mobile):
	print("列表页2视图")
	return HttpResponse("手机号：%s<br> <img src='/static/avatars/3.jpg'>列表页" % mobile)

# 可以接受多个参数，不仅是一两个。
def list3(request,cat,pn):
	return HttpResponse("cat=%s pn=%s" % (cat,pn) )

# 未分组
def index3(request, number):
    return HttpResponse('%s 正则表达式333' % number)

```





## 09-路由反解析和命名空间

在使用Django 项目时，一个常见的需求是获得 URL 的最终形式，以用于嵌入到生成的内容中（视图中和显示给用户的URL等）或者用于处理服务器端的导航（重定向等）。人们强烈希望不要硬编码这些URL（费力、不可扩展且容易产生错误）或者设计一种与URLconf 毫不相关的专门的URL 生成机制，因为这样容易导致一定程度上产生过期的URL

**注意：路由反解析和命名空间是相对于django后台调用来说的，前端用户还是和之前一样，该怎么访问就怎么访问**



#### 09.1 路由反解析

1.在子项目的 urls.py 路由文件中配置

```python
from django.urls import path, re_path
from students import views

urlpatterns = [
    path("index2/", views.index2, name='index_rev'),  # name 配置反向解析
    path("index5/", views.index5),
]

```

2.在子项目 views.py 视图文件中配置

```python
from django.shortcuts import HttpResponse, redirect,reverse

def index2(request):
    return HttpResponse('正则表达式xxx')

def index5(request):
    # 直接反向解析返回URL，哪怕index2这个视图函数和路由中的配置改变，只要name反向解析名称不变，就不会影响index5这个视图
    url = reverse("index_rev")  
    return redirect(url)

```



#### 09.2 命名空间

命名空间（英语：Namespace）是表示标识符的可见范围。一个标识符可在多个命名空间中定义，它在不同命名空间中的含义是互不相干的。这样，在一个新的命名空间中可定义任何标识符，它们不会与任何已有的标识符发生冲突，因为已有的定义都处于其它命名空间中。

由于name没有作用域，Django在反解URL时，会在项目全局顺序搜索，当查找到第一个name指定URL时，立即返回。

我们在开发项目时，会经常使用name属性反解出URL，当不小心在不同的app的urls中定义相同的name时，可能会导致URL反解错误，为了避免这种事情发生，引入了命名空间。

1.在主应用中的urls.py 文件中配置

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("students/", include("students.urls", namespace='stu_space')),  # namespace 命名空间
]
```

2.在子应用的urls.py 文件中配置

```python
from django.urls import path, re_path
from students import views

app_name = "stu_space"  # 命名空间，在django2.2 版本中需要加入，不然会报错

urlpatterns = [
    path("index2/", views.index2, name='index_rev'),  # name 配置反向解析
    path("index5/", views.index5),
]
```

3.在子应用视图文件中配置 views.py

```python
from django.shortcuts import HttpResponse, redirect,reverse

def index2(request):
    return HttpResponse('正则表达式xxx')

def index5(request):
    # 直接反向解析返回URL，哪怕index2这个视图函数和路由中的配置改变，只要name反向解析名称不变，就不会影响index5这个视图
    url = reverse("stu_space:index_rev")  # 注意此处，加入了命名空间
    return redirect(url)
```



#### 09.3 小案例

输入账号密码，登录成功跳转到另外一个网页显示登录成功，失败则直接返回登录失败。用到了命名空间和URL反向解析

1.子项目urls.py文件

```python
from django.urls import path
from students import views

app_name = "stu_space"  # 命名空间

urlpatterns = [
    path("index2/", views.index2, name='index_rev'),
    path("index5/", views.index5),
    path("login/", views.login, name='login_rev'),
]
```

2.子项目views.py文件

```python
from django.shortcuts import render, HttpResponse, redirect,reverse

def index2(request):
    return HttpResponse('登录成功')

def login(request):
    if request.method == "POST":
        usernmae = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if usernmae == "alex" and pwd == "123":
            return redirect(reverse("stu_space:index_rev"))
        else:
            return HttpResponse('登录失败')

    return render(request, 'login.html')

```

3.templates/ 目录下模板文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form action="{% url 'stu_space:login_rev' %}" method="post">
    {% csrf_token %}
    <p>用户名：<input type="text" name="user"></p>
    <p>密码：<input type="password" name="pwd"></p>
    <input type="submit">
</form>

</body>
</html>
```







## 10-请求

request有提供了5种方式给我们获取客户端发送过来的数据



#### 10.1-提取URL的特定部分

两个简便的方式可以完成：

+ 未命名参数

  路由文件中通过正则的小括号提取需要的路由信息：

  ```python
  from django.urls import re_path
  re_path("^list4/([a-z\d]+)/([a-z\d]+)$",views.list4 ),
  ```

  视图函数中request参数后面新增对应数量的形参用于接收数据

  ```python
  def list4(request, user, password):  # 可以接收多个参数
      return HttpResponse("user = %s <br> password = %s" % (user, password))
  
  ```

+ 命名参数

  在未命名参数 的左边圆括号后面加上?P<参数名称>.

```
from django.urls import re_path
re_path(r"list4/(?P<user>[a-z\d]+)/(?P<password>[a-z\d]+)$",views.list4 ),
```

​	在视图中获取命名参数

```python
def list4(request, user, password):  # 可以接收多个参数，但是需要和路由中的命名一致
    return HttpResponse("user = %s <br> password = %s" % (user, password))
```

访问：http://127.0.0.1:8000/students/list4/alnk/p123456

![assets/222.jpg](/assets/222.png)



#### 10.2-查询字符串（query string)

建议使用 postman 工具，可以模拟发送各种请求，例如：get、post、put、patch、delete等

+ request.GET.get() 获取单个查询字符串的参数 ，支持两种写法。

  ```python
  def list6(request):
      # 浏览器访问方式：http://127.0.0.1:8000/students/list6/?name=xiaoming&del=1&del=2
      
      """
      获取查询字符串
      :param request:客户端请求对象，里面包含了所有提交过来的请求信息
      :return:
      """
      # 获取客户端请求行中的查询字符串
      print(request.GET)
      # 打印效果：
      # 返回的结果是一个对象，我们可以看做是一个类字典对象
      # <QueryDict: {'name': ['xiaoming']}>
  
      # [少用]获取查询字符串中的指定名称的参数值[一个值],如果该值不存在就报错
      # print( request.GET["name"] )
  
      # [常用]获取查询字符串中的指定名称的参数值[一个值]
      print(request.GET.get("name", "佚名"))
  
      # getlist 获取查询字符串中的指定名称的参数值[多个值]
      print(request.GET.get("del"))  # 2 只会获取最后一个值
      print(request.GET.getlist("del"))  # ['1', '2']
  
      return HttpResponse("list6")
  ```

  ![](E:\python3周末班2期笔记\15 day15\01 老师笔记\assets\11.png)

+ request.GET.getlist() 获取多个查询字符串的参数

  ```python
      # getlist 获取查询字符串中的指定名称的参数值[多个值]
      print(request.GET.get("del"))  # ['2'] 只会获取最后一个值
      print(request.GET.getlist("del"))  # ['1', '2']
  ```



#### 10.3-请求体（body）

+ 表单类型数据，只能获取 method="post" 的数据

  ```python
  def list7(request):
      # 注意，post请求，暂时先把settings的csrf关掉
  
      """
      获取请求内容
      :param request:
      :return:
      """
      # 获取请求内容
      print(request.POST)
      # 打印效果：
      # reuqest.POST 返回结果和request.GET一致,，也是QueryDict对象
      # <QueryDict: {'name': ['xiaoming'], 'password': ['123']}>
  
      print(request.POST["username"])  # 如果不存在就报错
      print(request.POST.get("username", "默认值"))
  	
      # 获取多个值
      print(request.POST.getlist("like"))  # ['游泳', '电脑']
  
      # 获取上传文件信息
      # <MultiValueDict: {'file': [<InMemoryUploadedFile: api-ms-win-core-console-l1-1-0.dll (application/x-msdownload)>]}>
      print(request._files)  
      
      return HttpResponse("list6")
  ```

![](assets\12.png)

![](assets\13.png)

+ 非表单类型数据[ajax]

  ```python
  def list8(request):
      """
      获取请求内容[其他格式内容]
      # 其他格式数据: json/xml
      :param request:
      :return:
      """
      print(request.body)
      # request.body接受到数据，是bytes类型的数据
      # b'{\n\t"username":"xiaoming",\n\t"age":32,\n\t"achievement":13.5,\n\t"son":{\n\t\t"usernmae":"xxm",\n\t\t"age":12,\n\t\t"love":["\xe5\x90\x83","\xe5\x96\x9d"]\n\t}\n}'
  
      # 我们需要手动对请求体中的数据进行识别转换
      data_str = request.body.decode()
      print(data_str)
      print(type(data_str))
  
      import json
      data_dict = json.loads(data_str)  # <class 'str'>
      print(data_dict)
      print(type(data_dict))  # <class 'dict'>
  
      return HttpResponse('获取请求内容')
  ```

![](assets\14.png)



#### 10.4-请求头信息（header）

+ 自定义请求头信息

  ```python
  def list9(request):
      """
      获取请求头
      :param request:
      :return:
      """
      # http的请求头
      print(request.META.get("REQUEST_METHOD"))  # http 请求方法 GET
  
      # 自定义请求头[postman的请求头不支持中文]
      # 请求头名称必须大写,前面拼接 "HTTP_"
      print(request.META.get("HTTP_COMPANY"))  # JOYANY
  
      print(request.META)
      # 客户端信息,服务器信息,服务器系统信息[环境变量],python解析器相关信息
      # """
      # {
      #   'OS': 'Windows_NT',
      #   'SERVER_PORT': '8000',
      #   'REMOTE_HOST': '',
      #   'SCRIPT_NAME': '',
      #   'REQUEST_METHOD': 'GET',
      #   'PATH_INFO': '/home/detail4/',
      #   'QUERY_STRING': '',
      #   'REMOTE_ADDR': '127.0.0.1',
      #   'CONTENT_TYPE': 'text/plain',
      #   'HTTP_USER_AGENT': 'PostmanRuntime/7.13.0',
      #   'HTTP_HOST': '127.0.0.1:8000',
      # """
  
      return HttpResponse("获取请求头信息")
  ```

![](assets\15.png)



#### 10.5-其他的request请求信息

+ request.method

+ request.user

+ request.FILES

```python
def list10(request):
    """
    request对象的其他属性
    :param request:
    :return:
    """
    # print( request.method)  # 获取http请求方法, 等同于 request.META.get("REQUEST_METHOD")
    # print(request.FILES)    # 获取上传文件信息，等同于 request._files

    # 获取已经登录的用户信息[模型对象]
    print(request.user)  # 没有登录的用户访问,request.user = AnonymousUser

    # 获取登录用户的信息[如果没有登录,则报错]
    # print(request.user.last_login)

    return HttpResponse("request对象的其他属性")
```

![](assets\16.png)





## 11-响应

#### 11.1-内容响应

+ 响应html文本信息

  ```python
  HttpResponse(content="响应内容",content_type="内容类型，常见的有application/json,text/text",status="状态码,常见的有：404,200,201,204")
  
  # 还可以设置响应的响应头信息
  response = HttpResponse()
  response["company"] = "我的公司"
  return response
  ```

+ 响应其他信息[json]

```python
# 把字典数据响应成json格式数据
dict1 = {
  "name":"xiaobai",
  "age":21
}

# return HttpResponse(str(dict1),content_type="application/json")
return JsonResponse(dict1)

# 如果要响应的数据格式是列表.
list2 = ["xiaoming","xiaohei"]
return JsonResponse(list2)
```

```python
def res1(request):
    #响应html文档内容
    # return HttpResponse("<h1>响应内容</h1>")
    # return HttpResponse(content="<h1>响应内容</h1>",content_type="text/plain; charset=utf-8")

    # 响应json
    # data_dict = {
    #     "name": "xiaohong",
    #     "age": 15
    # }
    # import json
    # data_json = json.dumps(data_dict)
    # print(data_json)
    # return HttpResponse(content=data_json,content_type="application/json")

    # 响应xml数据
    data_xml = """<xml version="1.0" encoding="utf-8"><name>小红</name><age>15</age></xml>"""
    return HttpResponse(content=data_xml, content_type="text/xml")
```

![](assets\17.png)

![](assets\18.png)

![](assets\19.png)



#### 11.2-页面跳转

也叫页面重定向

```python
# shortcuts 简写函数库
from django.shortcuts import redirect
def res2(request):
	"""页面重定向响应"""
	# return redirect("http://www.baidu.com")

	# redirect 其实本质上就是 HttpResponse的简写操作,以下是还原代码:
	response = HttpResponse(status=302)
	response["Location"] = "http://www.baidu.com"
	return response
```





## 12-扩展内容

前后端传递数据时，数据的格式可以是html文本格式，json格式，xml格式。当然不同平台，不同的编程语言也是如此。

+ 文本格式：

  ```text
  username=小明&password=123456
  ```

+ json格式：

  ```json
  {
      "username":"小明",
      "password":"123456",
      "sex":"女"
  }
  ```

+ xml格式：

  xml格式类似于html，也是采用标签来表达数据的，但是不一样的是，xml的所有标签都需要开发者自定义。

  现在使用这种格式的公司很少了。

  ```
  <xml version="1.0" charset="utf-8">
  	<username>小明</username>
  	<password>123456</password>
  	<sex>女</sex>
  </xml>
  ```

