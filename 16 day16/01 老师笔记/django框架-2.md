用户角度：

​	打开登陆页面

​	输入账号密码

​	点击登陆按钮

​	跳转到目标页面

开发者角度

​	提供一个视图1函数给用户访问[绑定路由]

​        在视图1中加载页面，显示表单

​        提供与一个视图2给用户提交账号密码[绑定路由]

​        在视图2中操作数据库获取当前账号密码对应的信息。如果获取不到，则无法登陆。



# 视图

## 函数视图[Function Base View]

以函数的方式定义的视图称为**函数视图**，函数视图便于理解。但是遇到一个视图对应的路径提供了多种不同HTTP请求方式的支持时，便需要在一个函数中编写不同的业务逻辑，代码可读性与复用性都不佳。

```python
 def register(request):
    """处理注册"""

    # 获取请求方法，判断是GET/POST请求
    if request.method == 'GET':
        # 处理GET请求，返回注册页面
        return render(request, 'register.html')
    else:
        # 处理POST请求，实现注册逻辑
        return HttpResponse('这里实现注册逻辑')
```





## 类视图[Class Base View]

在Django中也可以使用类来定义一个视图，称为**类视图**。

使用类视图可以将视图对应的不同请求方式以类中的不同方法来区别定义。如下所示

```python
"""
# django的类视图一共提供了多个以http请求方法命名的类方法给我们使用。
# 当客户端使用不同的http请求方法访问当前视图类，django会根据请求方法访问到当前类视图中的同名对象方法中。
# http常用请求方法
# GET    客户端向服务端请求读取数据
# POST   客户端向服务器请求创建数据
# PUT    客户端向服务器请求修改数据[全部]
# PATCH  客户端向服务器请求修改数据[修改部分数据]
# DELETE 客户端向服务器请求删除数据
"""
from django.views import View
from django.http.response import HttpResponse
class UserView(View):
	def post(self,request):
		print("客户端进行post请求")
		return HttpResponse("post")

	def get(self,request):
		print("客户端进行get请求")
		return HttpResponse("get")

	def put(self,request):
		print("客户端进行put请求")
		return HttpResponse("put")

	def delete(self,request):
		print("客户端进行delete请求")
		return HttpResponse("delete")
```

类视图的好处：

- **代码可读性好**
- **类视图相对于函数视图有更高的复用性**， 如果其他地方需要用到某个类视图的某个特定逻辑，直接继承该类视图即可



### 类视图使用

定义类视图需要继承自Django提供的父类**View**，可使用`from django.views.generic import View`或者`from django.views.generic.base import View` 导入，定义方式如上所示。

**配置路由时，使用类视图的as_view()方法来添加**。

```python
from django.urls import path
from . import views
urlpatterns = [
	path("cls/", views.UserView.as_view() ),
]
```



### 类视图原理

```python
    @classonlymethod
    def as_view(cls, **initkwargs):
        """
        Main entry point for a request-response process.
        """
        ...省略代码...

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.request = request
            self.args = args
            self.kwargs = kwargs
            # 调用dispatch方法，按照不同请求方式调用不同请求方法
            return self.dispatch(request, *args, **kwargs)

        ...省略代码...

        # 返回真正的函数视图
        return view


    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
```



###  类视图使用装饰器

为类视图添加装饰器，可以使用三种方法。

为了理解方便，我们先来定义一个**为函数视图准备的装饰器**（在设计装饰器时基本都以函数视图作为考虑的被装饰对象），及一个要被装饰的类视图。

```python
def my_decorator(func):
	def wrapper(request, *args, **kwargs):
		print('自定义装饰器被调用了')
		print('请求路径%s' % request.path)
		return func(request, *args, **kwargs)
	return wrapper

class DemoView(View):
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self, request):
        print('post方法')
        return HttpResponse('ok')
```



#### 在URL配置中装饰

```python
urlpatterns = [
    url(r'^demo/$', my_decorate(views.UAPI2.as_view()))
]
```

此种方式最简单，但因装饰行为被放置到了url配置中，单看视图的时候无法知道此视图还被添加了装饰器，不利于代码的完整性，不建议使用。

**此种方式会为类视图中的所有请求方法都加上装饰器行为**（因为是在视图入口处，分发请求方式前）。



#### 在类视图中装饰

在类视图中使用为函数视图准备的装饰器时，不能直接添加装饰器，需要使用**method_decorator**将其转换为适用于类视图方法的装饰器。

```python
from django.utils.decorators import method_decorator

# 为全部请求方法添加装饰器
class DemoView(View):

    @method_decorator(my_decorator)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self, request):
        print('post方法')
        return HttpResponse('ok')


# 为特定请求方法添加装饰器
class DemoView(View):

    @method_decorator(my_decorator)
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self, request):
        print('post方法')
        return HttpResponse('ok')
```

**method_decorator装饰器还支持使用name参数指明被装饰的方法**

```python
# 为全部请求方法添加装饰器
@method_decorator(my_decorator, name='dispatch')
class DemoView(View):
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self, request):
        print('post方法')
        return HttpResponse('ok')


# 为特定请求方法添加装饰器
@method_decorator(my_decorator, name='get')
class DemoView(View):
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self, request):
        print('post方法')
        return HttpResponse('ok')
```

##### method_decorator

为函数视图准备的装饰器，其被调用时，第一个参数用于接收request对象

```python
def my_decorate(func):
    def wrapper(request, *args, **kwargs):  # 第一个参数request对象
        ...代码省略...
        return func(request, *args, **kwargs)
    return wrapper
```

而类视图中请求方法被调用时，传入的第一个参数不是request对象，而是self 视图对象本身，第二个位置参数才是request对象

```python
class DemoView(View):
    def dispatch(self, request, *args, **kwargs):
        ...代码省略...

    def get(self, request):
        ...代码省略...
```

所以如果直接将用于函数视图的装饰器装饰类视图方法，会导致参数传递出现问题。

**method_decorator的作用是为函数视图装饰器补充第一个self参数，以适配类视图方法。**

如果将装饰器本身改为可以适配类视图方法的，类似如下，则无需再使用method_decorator。

```python
def my_decorator(func):
    def wrapper(self, request, *args, **kwargs):  # 此处增加了self
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(self, request, *args, **kwargs)  # 此处增加了self
    return wrapper
```



#### 构造Mixin扩展类

使用面向对象多继承的特性。

```python
class MyDecoratorMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator(view)
        return view

class DemoView(MyDecoratorMixin, View):
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self, request):
        print('post方法')
        return HttpResponse('ok')
```



使用Mixin扩展类，也会为类视图的所有请求方法都添加装饰行为。**

```python
"""在多个类视图中如果要公用代码，可以使用多继承[Mixin扩展类]"""
@method_decorator(my_decorator,name='dispatch')
class BaseView(View):
	pass

class UAPI4(BaseView):
	def get(self,request):
		return HttpResponse("类视图4get方法使用装饰器")

	def post(self,request):
		return HttpResponse("类视图4post方法使用装饰器")

```



# 中间件

中间件[middleware],也叫钩子方法[钩子函数],hook

Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出。中间件的设计为开发者提供了一种无侵入式的开发方式，增强了Django框架的健壮性。

我们可以使用中间件，在Django处理视图的不同阶段对输入或输出进行干预。



## 中间件的定义方法

中间件工厂函数需要接收一个可以调用的get_response对象。

返回的中间件也是一个可以被调用的对象，并且像视图一样需要接收一个request对象参数，返回一个response对象。

```python
def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。

        return response

    return middleware
```

例如，在主应用中新建一个middlewares.py文件，

```python
def simple_middleware(get_response):
	# 项目启动时执行的代码。
	print("__init__项目初始化")

	# 这个子函数会在用户请求的时候才会执行
	def middleware(request):
		# 此处编写的代码会在每个请求处理视图前被调用。
		print("视图执行请求之前的代码,解密,验证权限")
		response = get_response(request)

		# 此处编写的代码会在每个请求处理视图之后被调用。
		print("视图执行响应之后的代码,加密,操作记录")
		return response

	return middleware
```



**定义好中间件后，需要在settings.py 文件中添加注册中间件**

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.my_middleware',  # 添加中间件
]
```



**注意：Django运行在调试模式下，中间件init部分有可能被调用两次。**



## 多个中间件的执行顺序

- 在请求视图被处理**前**，中间件**由上至下**依次执行
- 在请求视图被处理**后**，中间件**由下至上**依次执行



示例：

定义两个中间件

```python
def my_middleware(get_response):
    print('init 被调用')
    def middleware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after response 被调用')
        return response
    return middleware

def my_middleware2(get_response):
    print('init2 被调用')
    def middleware(request):
        print('before request 2 被调用')
        response = get_response(request)
        print('after response 2 被调用')
        return response
    return middleware
```

注册添加两个中间件

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.my_middleware',  # 添加
    'users.middleware.my_middleware2',  # 添加
]
```

执行结果

```python
init2 被调用
init 被调用
before request 被调用
before request 2 被调用
view 视图被调用
after response 2 被调用
after response 被调用
```



# 数据库

## ORM框架

O是object，也就**类对象**的意思。

R是relation，翻译成中文是关系，也就是关系数据库中**数据表**的意思。

M是mapping，是**映射**的意思。

ORM框架会帮我们把类对象和数据表进行了一对一的映射，让我们可以**通过类对象来操作对应的数据表**。

ORM框架还可以**根据我们设计的类自动帮我们生成数据库中的表格**，省去了我们自己建表的过程。

django中内嵌了ORM框架，不需要直接编写SQL语句进行数据库操作，而是通过定义模型类，操作模型类来完成对数据库中表的增删改查和创建等操作。

![orm](.\assets\orm2.png)



### ORM的优点

> - 数据模型都在一个地方定义，更容易更新和维护，也利于重用代码。
> - ORM 有现成的工具，很多功能都可以自动完成，比如数据消毒、预处理、事务等等。
> - 它迫使你使用 MVC 架构，ORM 就是天然的 Model，最终使代码更清晰。
> - 基于 ORM 的业务代码比较简单，代码量少，语义性好，容易理解。
> - 你不必编写性能不佳的 SQL。

### ORM 也有缺点

> - ORM 库不是轻量级工具，需要花很多精力学习和设置，甚至不同的框架，会存在不同操作的ORM。
> - 对于复杂的业务查询，ORM表达起来比原生的SQL要更加困难和复杂。
> - ORM操作数据库的性能要比使用原生的SQL差。
> - ORM 抽象掉了数据库层，开发者无法了解底层的数据库操作，也无法定制一些特殊的 SQL。



### 配置数据库连接

在settings.py中保存了数据库的连接配置信息，Django默认初始配置使用**sqlite**数据库。

我们可以通过以下步骤来使用django的数据库操作

```text
1. 配置数据库连接信息
2. 在子用用的models.py中定义模型类
3. 生成数据库迁移文件并执行迁移文件
4. 通过模型类对象完成数据表的增删改查操作
```



1. 使用**MySQL**数据库首先需要安装驱动程序

   ```shell
   pip install PyMySQL
   ```

   

2. 在Django的工程同名子目录的`__init__.py`文件中添加如下语句

   ```python
   from pymysql import install_as_MySQLdb
   
   install_as_MySQLdb()
   ```

   作用是让Django的ORM能以mysqldb的方式来调用PyMySQL。

   

3. 修改**DATABASES**配置信息

   ```python
   # Database
   # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
   # 数据库配置
   DATABASES = {
       # 'default': {
       #     'ENGINE': 'django.db.backends.sqlite3',
       #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       # },
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': "djangodemo",
           'HOST':"localhost",
           'PORT':3306,
           "USER":"root",
           "PASSWORD":"123456",
       }
   }
   ```

   

4. 在MySQL中创建数据库

   ```mysql
   create database django_demo default charset=utf8mb4;
   ```



### 定义模型类

- 模型类被定义在"应用/models.py"文件中。
- 模型类必须继承自Model类，位于包django.db.models中。

接下来以学生管理为例进行演示。

#### 定义

创建应用student，在models.py 文件中定义模型类。

```python
from django.db import models

#定义学生模型类Student
class Student(models.Model):
    SEX_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=0, verbose_name='性别')
    class_no = models.IntegerField(verbose_name='班级')
    description = models.TextField(null=True,verbose_name='个性签名')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_student'  # 指明数据库表名
        verbose_name = '学生信息表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
```

**1） 数据库表名**

模型类如果未指明表名，Django默认以 **小写app应用名_小写模型类名** 为数据库表名。

可通过**db_table** 指明数据库表名。

**2） 关于主键**

django会为表创建自动增长的主键列，每个模型只能有一个主键列。

如果使用选项设置某属性为主键列后，django不会再创建自动增长的主键列。

默认创建的主键列属性为id，可以使用<mark>pk</mark>代替，pk全拼为<mark>primary key</mark>。

**3） 属性命名限制**

- 不能是python或者mysql的保留关键字。

- 不允许使用连续的下划线，这是由django的查询方式决定的。

- 定义属性时需要指定字段类型，通过字段类型的参数指定选项，语法如下：

  ```python
  属性=models.字段类型(选项)
  ```

**4）字段类型**

| 类型             | 说明                                                         |
| :--------------- | :----------------------------------------------------------- |
| AutoField        | 自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性 |
| BooleanField     | 布尔字段，值为True或False                                    |
| NullBooleanField | 支持Null、True、False三种值                                  |
| CharField        | 字符串，参数max_length表示最大字符个数                       |
| TextField        | 大文本字段，一般大段文本（超过4000个字符）才使用。           |
| IntegerField     | 整数                                                         |
| DecimalField     | 十进制浮点数,例如价格， 参数max_digits表示总位数， 参数decimal_places表示小数位数 |
| FloatField       | 浮点数，参数同DecimalField                                   |
| DateField        | 日期<br>参数auto_now表示每次保存对象时，自动设置该字段为当前时间。<br>参数auto_now_add表示当对象第一次被创建时自动设置当前。<br>参数auto_now_add和auto_now是相互排斥的，一起使用会发生错误。 |
| TimeField        | 时间，参数同DateField                                        |
| DateTimeField    | 日期时间，参数同DateField                                    |
| FileField        | 上传文件字段                                                 |
| ImageField       | 继承于FileField，对上传的内容进行校验，确保是有效的图片      |



**5） 选项**

| 选项        | 说明                                                         |
| :---------- | ------------------------------------------------------------ |
| null        | 如果为True，表示允许为空，默认值是False。                    |
| blank       | 如果为True，则该字段允许为空白，默认值是False。              |
| db_column   | 字段的名称，如果未指定，则使用属性的名称。                   |
| db_index    | 若值为True, 则在表中会为此字段创建索引，默认值是False。      |
| default     | 默认值，当不填写数据时，使用该选项的值作为数据的默认值。     |
| primary_key | 如果为True，则该字段会成为模型的主键，默认值是False，一般不用设置，系统默认设置。 |
| unique      | 如果为True，则该字段在表中必须有唯一值，默认值是False。      |

**注意：null是数据库范畴的概念，blank是表单验证范畴的**



**6） 外键**ForeignKey

在设置外键时，需要通过**on_delete**选项指明主表删除数据时，对于外键引用表数据如何处理，在django.db.models中包含了可选常量：

- **CASCADE** 级联，删除主表数据时连通一起删除外键表中数据

- **PROTECT** 保护，通过抛出**ProtectedError**异常，来阻止删除主表中被外键应用的数据

- **SET_NULL** 设置为NULL，仅在该字段null=True允许为null时可用

- **SET_DEFAULT** 设置为默认值，仅在该字段设置了默认值时可用

- **SET()** 设置为特定值或者调用特定方法，例如：

  ```python
  from django.conf import settings
  from django.contrib.auth import get_user_model
  from django.db import models
  
  def get_sentinel_user():
      return get_user_model().objects.get_or_create(username='deleted')[0]
  
  class UserModel(models.Model):
      user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.SET(get_sentinel_user),
      )
  ```

- **DO_NOTHING** 不做任何操作，如果数据库前置指明级联性，此选项会抛出**IntegrityError**异常



#### 数据迁移

注意，对子应用里面的models.py进行数据迁移之前，必须先查看当前子应用是否已经在`settings.py`的`INSTALL_APPS`中注册了，所以没有注册，则无法对当前子应用的models.py进行迁移。



将模型类同步到数据库中。

**1）生成迁移文件**

```python
python manage.py makemigrations
```

**2）同步到数据库中**

```python
python manage.py migrate
```

#### 3 添加测试数据

```sql
INSERT INTO `tb_student`(id,name,sex,class_no,age,description,money,is_delete,born)VALUES
(1,'赵华',1,307,22,'对于勤奋的人来说，成功不是偶然；对于懒惰的人来说，失败却是必然。',10,0,'1996-10-01'),
(2,'程星云',1,301,20,'人生应该如蜡烛一样，从顶燃到底，一直都是光明的。',10,0,'1996-10-01'),
(3,'陈峰',1,504,21,'在不疯狂，我们就老了，没有记忆怎么祭奠呢？',10,0,'1996-10-01'),
(4,'苏礼就',1,502,20,'不要为旧的悲伤，浪费新的眼泪。',10,0,'1996-10-01'),
(5,'张小玉',2,306,18,'没有血和汗水就没有成功的泪水。',10,0,'1996-10-01'),
(6,'吴杰',1,307,19,'以大多数人的努力程度之低，根本轮不到去拼天赋',10,0,'1996-10-01'),
(7,'张小辰',2,405,19,'人生的道路有成千上万条， 每一条路上都有它独自的风景。',10,0,'1996-10-01'),
(8,'王丹丹',2,502,22,'平凡的人听从命运，坚强的人主宰命运。',10,0,'1996-10-01'),
(9,'苗俊伟',1,503,22,'外事找谷歌，内事找百度。',10,0,'1996-10-01'),
(10,'娄镇明',1,301,22,'不经三思不求教，不动笔墨不读书。',10,0,'1996-10-01'),
(11,'周梦琪',2,306,19,'学习与坐禅相似，须有一颗恒心。',10,0,'1996-10-01'),
(12,'欧阳博',1,503,23,'春去秋来，又一年。What did you get ?',10,0,'1996-10-01'),
(13,'颜敏莉',2,306,20,'Knowledge makes humble, ignorance makes proud.',10,0,'1996-10-01'),
(14,'柳宗仁',1,301,20,'有志者事竟成。',10,0,'1996-10-01'),
(15,'谢海龙',1,402,22,'这世界谁也不欠谁，且行且珍惜。',10,0,'1996-10-01'),
(16,'邓士鹏',1,508,22,'青，取之于蓝而青于蓝；冰，水为之而寒于水。',10,0,'1996-10-01'),
(17,'宁静',2,502,23,'一息若存 希望不灭',10,0,'1996-10-01'),
(18,'上官屏儿',2,502,21,'美不自美,因人而彰。',10,0,'1996-10-01'),
(19,'孙晓静',2,503,20,'人生本过客，何必千千结；无所谓得失，淡看风和雨。',10,0,'1996-10-01'),
(20,'刘承志',1,306,20,'good good study,day day up! ^-^',10,0,'1996-10-01'),
(21,'王浩',1,503,21,'积土而为山，积水而为海。',10,0,'1996-10-01'),
(22,'钟无艳',2,303,19,'真者，精诚之至也，不精不诚，不能动人。',10,0,'1996-10-01'),
(23,'莫荣轩',1,409,22,'不管发生什么事，都请安静且愉快地接受人生，勇敢地、大胆地，而且永远地微笑着。',10,0,'1996-10-01'),
(24,'张裕民',1,303,21,'伟大的目标形成伟大的人物。',10,0,'1996-10-01'),
(25,'江宸轩',1,407,22,'用最少的悔恨面对过去。',10,0,'1996-10-01'),
(26,'谭季同',1,305,21,'人总是珍惜未得到的，而遗忘了所拥有的。',10,0,'1996-10-01'),
(27,'李松风',1,504,19,'明天的希望，让我们忘了今天的痛苦。',10,0,'1996-10-01'),
(28,'叶宗政',1,407,20,'因害怕失败而不敢放手一搏，永远不会成功。',10,0,'1996-10-01'),
(29,'魏雪宁',2,306,20,'成功与失败只有一纸之隔',10,0,'1996-10-01'),
(30,'徐秋菱',2,404,19,'年轻是我们唯一拥有权利去编织梦想的时光。',10,0,'1996-10-01'),
(31,'曾嘉慧',2,301,19,'有一分热，发一分光。就令萤火一般，也可以在黑暗里发一点光，不必等候炬火。',10,0,'1996-10-01'),
(32,'欧阳镇安',1,408,23,'青春虚度无所成，白首衔悲补何及!',10,0,'1996-10-01'),
(33,'周子涵',2,309,19,'青春是一个普通的名称，它是幸福美好的，但它也是充满着艰苦的磨炼。',10,0,'1996-10-01'),
(34,'宋应诺',2,501,23,'涓滴之水终可以磨损大石，不是由于它力量强大，而是由于昼夜不舍的滴坠。',10,0,'1996-10-01'),
(35,'白瀚文',1,305,19,'一个人假如不脚踏实地去做，那么所希望的一切就会落空。',10,0,'1996-10-01'),
(36,'陈匡怡',2,505,19,'一份耕耘，一份收获。',10,0,'1996-10-01'),
(37,'邵星芸',2,503,22,'冰冻三尺非一日之寒。',10,0,'1996-10-01'),
(38,'王天歌',2,302,21,'任何的限制，都是从自己的内心开始的。',10,0,'1996-10-01'),
(39,'王天龙',1,302,22,'再长的路，一步步也能走完，再短的路，不迈开双脚也无法到达。',10,0,'1996-10-01'),
(40,'方怡',2,509,23,'智者不做不可能的事情。',10,0,'1996-10-01'),
(41,'李伟',1,505,19,'人之所以能，是相信能。',10,0,'1996-10-01'),
(42,'李思玥',2,503,22,'人的一生可能燃烧也可能腐朽，我不能腐朽，我愿意燃烧起来。',10,0,'1996-10-01'),
(43,'赵思成',1,401,18,'合抱之木，生于毫末;九层之台，起于累土。',10,0,'1996-10-01'),
(44,'蒋小媛',2,308,22,'不积跬步无以至千里，不积细流无以成江河。',10,0,'1996-10-01'),
(45,'龙华',1,510,19,'只要持续地努力，不懈地奋斗，就没有征服不了的东西。',10,0,'1996-10-01'),
(46,'牧婧白夜',2,501,21,'读不在三更五鼓，功只怕一曝十寒。',10,0,'1996-10-01'),
(47,'江俊文',1,304,19,'立志不坚，终不济事。',10,0,'1996-10-01'),
(48,'李亚容',2,304,18,'Keep on going never give up.',10,0,'1996-10-01'),
(49,'王紫伊',2,301,22,'最可怕的敌人，就是没有坚强的信念。',10,0,'1996-10-01'),
(50,'毛小宁',1,501,19,'要从容地着手去做一件事，但一旦开始，就要坚持到底。',10,0,'1996-10-01'),
(51,'董 晴',2,507,19,'常常是最后一把钥匙打开了门。贵在坚持',10,0,'1996-10-01'),
(52,'严语',2,405,18,'逆水行舟，不进则退。',10,0,'1996-10-01'),
(53,'陈都灵',2,503,19,'无论什么时候，不管遇到什么情况，我绝不允许自己有一点点灰心丧气。',10,0,'1996-10-01'),
(54,'黄威',1,301,23,'我的字典里面没有“放弃”两个字',10,0,'1996-10-01'),
(55,'林佳欣',2,308,23,'梦想就是一种让你感到坚持,就是幸福的东西。',10,0,'1996-10-01'),
(56,'翁心颖',2,303,19,'有目标的人才能成功，因为他们知道自己的目标在哪里。',10,0,'1996-10-01'),
(57,'蒙毅',1,502,22,'所谓天才，就是努力的力量。',10,0,'1996-10-01'),
(58,'李小琳',2,509,22,'每天早上对自己微笑一下。这就是我的生活态度。',10,0,'1996-10-01'),
(59,'伍小龙',1,406,19,'一路上的点点滴滴才是我们的财富。',10,0,'1996-10-01'),
(60,'晁然',2,305,23,'人的价值是由自己决定的。',10,0,'1996-10-01'),
(61,'端木浩然',1,507,18,'摔倒了爬起来再哭。',10,0,'1996-10-01'),
(62,'姜沛佩',2,309,21,'Believe in yourself.',10,0,'1996-10-01'),
(63,'李栋明',1,306,19,'虽然过去不能改变，但是未来可以。',10,0,'1996-10-01'),
(64,'柴柳依',2,508,23,'没有实践就没有发言权。',10,0,'1996-10-01'),
(65,'吴杰',1,401,22,'人生有两出悲剧。一是万念俱灰;另一是踌躇满志',10,0,'1996-10-01'),
(66,'杜文华',1,507,19,'有智者立长志，无志者长立志。',10,0,'1996-10-01'),
(67,'邓珊珊',2,510,18,'Action is the proper fruit of knowledge.',10,0,'1996-10-01'),
(68,'杜俊峰',1,507,23,'世上无难事，只要肯登攀。',10,0,'1996-10-01'),
(69,'庄信杰',1,301,22,'知识就是力量。',10,0,'1996-10-01'),
(70,'宇文轩',1,402,23,'如果你想要某样东西，别等着有人某天会送给你。生命太短，等不得。',10,0,'1996-10-01'),
(71,'黄佳怿',2,510,19,'Learn and live.',10,0,'1996-10-01'),
(72,'卫然',1,510,18,'神于天，圣于地。',10,0,'1996-10-01'),
(73,'耶律齐',1,307,23,'如果不是在海市蜃楼中求胜，那就必须脚踏实地去跋涉。',10,0,'1996-10-01'),
(74,'白素欣',2,305,18,'欲望以提升热忱，毅力以磨平高山。',10,0,'1996-10-01'),
(75,'徐鸿',1,403,23,'最美的不是生如夏花，而是在时间的长河里，波澜不惊。',10,0,'1996-10-01'),
(76,'上官杰',1,409,19,'生活之所以耀眼，是因为磨难与辉煌会同时出现。',10,0,'1996-10-01'),
(77,'吴兴国',1,406,18,'生活的道路一旦选定，就要勇敢地走到底，决不回头。',10,0,'1996-10-01'),
(78,'庄晓敏',2,305,18,'Never say die.',10,0,'1996-10-01'),
(79,'吴镇升',1,509,18,'Judge not from appearances.',10,0,'1996-10-01'),
(80,'朱文丰',1,304,19,'每个人都比自己想象的要强大，但同时也比自己想象的要普通。',10,0,'1996-10-01'),
(81,'苟兴妍',2,508,18,'Experience is the best teacher.',10,0,'1996-10-01'),
(82,'祝华生',1,302,21,'浅学误人。',10,0,'1996-10-01'),
(83,'张美琪',2,404,23,'最淡的墨水，也胜过最强的记性。',10,0,'1996-10-01'),
(84,'周永麟',1,308,21,'All work and no play makes Jack a dull boy.',10,0,'1996-10-01'),
(85,'郑心',2,404,21,'人生就像一杯茶，不会苦一辈子，但总会苦一阵子。',10,0,'1996-10-01'),
(86,'公孙龙馨',1,510,21,'Experience is the father of wisdom and memory the mother.',10,0,'1996-10-01'),
(87,'叶灵珑',2,401,19,'读一书，增一智。',10,0,'1996-10-01'),
(88,'上官龙',1,501,21,'别人能做到的事，自己也可以做到。',10,0,'1996-10-01'),
(89,'颜振超',1,303,19,'如果要飞得高，就该把地平线忘掉。',10,0,'1996-10-01'),
(90,'玛诗琪',2,409,22,'每天进步一点点，成功不会远。',10,0,'1996-10-01'),
(91,'李哲生',1,309,22,'这不是偶然的失误，是必然的结果。',10,0,'1996-10-01'),
(92,'罗文华',2,408,22,'好走的都是下坡路。',10,0,'1996-10-01'),
(93,'李康',1,509,19,'Deliberate slowly, promptly.',10,0,'1996-10-01'),
(94,'钟华强',1,405,19,'混日子很简单,讨生活比较难。',10,0,'1996-10-01'),
(95,'张今菁',2,403,23,'不经一翻彻骨寒，怎得梅花扑鼻香。',10,0,'1996-10-01'),
(96,'黄伟麟',1,407,19,'与其诅咒黑暗，不如燃起蜡烛。没有人能给你光明，除了你自己。',10,0,'1996-10-01'),
(97,'程荣泰',1,406,22,'明天不一定更好,。但更好的明天一定会来。',10,0,'1996-10-01'),
(98,'范伟杰',1,508,19,'水至清则无鱼，人至察则无徒。凡事不能太执着。',10,0,'1996-10-01'),
(99,'王俊凯',1,407,21,'我欲将心向明月,奈何明月照沟渠。',10,0,'1996-10-01'),
(100,'白杨 ',1,406,19,'闪电从不打在相同的地方.人不该被相同的方式伤害两次。',10,0,'1996-10-01');
```

 







## 数据库操作

### 增加数据

增加数据有两种方法。

**1）save**

通过创建模型类对象，执行对象的save()方法保存到数据库中。

```python
student = Student(
    name='刘德华',
    class_no='305',
    sex=0,
    age=18
)
student.save()
```

**2）create**

通过模型类.objects.create()保存。create更常用!

```python
Student.objects.create(
    name='刘德华',
    class_no='305',
    sex=0,
    age=18
)

# 打印结果：
# <Student: 刘德华>
```



### 查询

#### 1 基本查询

**get** 查询单一结果，如果不存在会抛出**模型类.DoesNotExist**异常。

**all** 查询多个结果。

**count** 查询结果数量。

```python
Student.objects.all()
# <QuerySet [<Student: 赵华>, <Student: 程星云>, <Student: 陈峰>, <Student: 苏礼就>..]>

student = Student.objects.get(name='赵华')
student.id
# 1

Student.objects.get(id=3)
# <Student: 陈峰>

Student.objects.get(pk=3)
# <Student: 陈峰>

Student.objects.get(id=200)
# 报错：
# db.models.DoesNotExist: Student matching query does not exist.

Student.objects.count()
101
```



#### 2 过滤查询

实现SQL中的where功能，包括

- **filter** 过滤出多个结果
- **exclude** 排除掉符合条件剩下的结果
- **get** 过滤单一结果

对于过滤条件的使用，上述三个方法相同，故仅以**filter**进行讲解。

过滤条件的表达语法如下：

```python
属性名__运算符=值
# 属性名称和比较运算符间使用两个下划线，所以属性名不能包括多个下划线
```

**1）相等**

**exact：表示判等。**

例：查询编号为1的学生。

```
Student.objects.filter(id__exact=1)
可简写为：
Student.objects.filter(id=1)
```



**2）模糊查询**

**contains：是否包含。**

> 说明：如果要包含%无需转义，直接写即可。

例：查询姓名包含'华'的学生。

```python
Student.objects.filter(name__contains='华')
```



**startswith、endswith：以指定值开头或结尾。**

例：查询姓名以'文'结尾的学生

```python
Student.objects.filter(name__endswith='文')
```

> 以上运算符都区分大小写，在这些运算符前加上i表示不区分大小写，如iexact、icontains、istartswith、iendswith.



**3） 空查询**

**isnull：是否为null。**

例：查询个性签名不为空的学生。

```python
Student.objects.filter(description__isnull=False)
```

**4） 范围查询**

**in：是否包含在范围内。**

例：查询编号为1或3或5的学生

```python
Student.objects.filter(id__in=[1, 3, 5])
```

**5）比较查询**

- **gt** 大于 (greater then)
- **gte** 大于等于 (greater then equal)
- **lt** 小于 (less then)
- **lte** 小于等于 (less then equal)

例：查询编号大于3的学生

```python
Student.objects.filter(id__gt=3)
```



**不等于的运算符，使用exclude()过滤器。**

例：查询编号不等于3的学生

```python
Student.objects.exclude(id=3)
```



**6）日期查询**

**year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算。**

例：查询1980年出生的学生。

```python
Student.objects.filter(born_date__year=1980)
```



例：查询1980年1月1日后出生的学生。

```python
Student.objects.filter(born__gt=date(1990, 1, 1))
```



##### F对象

之前的查询都是对象的属性与常量值比较，两个属性怎么比较呢？ 答：使用F对象，被定义在django.db.models中。

语法如下：

```
from django.db.models import F

模型对象.objects.filter(属性名1__gte=F('属性名2'))
```



##### Q对象

**多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字。**

例：查询年龄大于20，并且编号小于30的学生。

```python
Student.objects.filter(age__gt=20,id__lt=30)
或
Student.filter(age__gt=20).filter(id__lt=30)
```

**如果需要实现逻辑或or的查询，需要使用Q()对象结合|运算符**，Q对象被义在django.db.models中。

语法如下：

```
Q(属性名__运算符=值)
```

例：查询年龄大于20的学生，改写为Q对象如下。

```python
from django.db.models import Q

Student.objects.filter(Q(age__gt=20))
```



Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或****

例：查询年龄大于20，或编号小于30的学生，只能使用Q对象实现

```python
Student.objects.filter(Q(age__gt=20) | Q(pk__lt=30))
```

Q对象前可以使用~操作符，表示非not。

例：查询编号不等于30的学生。

```python
Student.objects.filter(~Q(pk=30))
```



##### 聚合函数

使用aggregate()过滤器调用聚合函数。聚合函数包括：**Avg** 平均，**Count** 数量，**Max** 最大，**Min** 最小，**Sum** 求和，被定义在django.db.models中。

例：查询学生的总年龄。

```python
from django.db.models import Sum

Student.objects.aggregate(Sum('age'))
```



注意：aggregate的返回值是一个字典类型，格式如下：

```python
  {'属性名__聚合类小写':值}
  如:{'bread__sum':3}
```



使用count时一般不使用aggregate()过滤器。

例：查询学生总数。

```python
Student.objects.count()
```

注意：count函数的返回值是一个数字。



#### 3 排序

使用**order_by**对结果进行排序

```python
Student.objects.all().order_by('age')  # 升序
Student.all().order_by('-age')  # 降序
```



连表查询以及关联查询的关联等级[下节课内容]



### 修改

修改更新有两种方法

**1）save**

**修改模型类对象的属性，然后执行save()方法**

```python
student = Student.objects.get(name='刘德华')
student.name = '周星星'
student.save()
```



**2）update**

**使用模型类.objects.filter().update()**，会返回受影响的行数

```python
Student.objects.filter(name='赵华').update(name='赵晓华')
```



### 删除

删除有两种方法

**1）模型类对象.delete**

```python
student = Student.objects.get(id=13)
student.delete()
```

**2）模型类.objects.filter().delete()**

```python
Student.objects.filter(id=14).delete()
```



## 查询集 QuerySet

查询集，也称查询结果集、QuerySet，表示从数据库中获取的对象集合。

当调用如下过滤器方法时，Django会返回查询集（而不是简单的列表）：

- all()：返回所有数据。
- filter()：返回满足条件的数据。
- exclude()：返回满足条件之外的数据。
- order_by()：对结果进行排序。

对查询集可以再次调用过滤器进行过滤，如

```python
Student.objects.filter(pk__gt=30).order_by('age')
```

也就意味着查询集可以含有零个、一个或多个过滤器。过滤器基于所给的参数限制查询的结果。

**从SQL的角度讲，查询集与select语句等价，过滤器像where、limit、order by子句。**

**判断某一个查询集中是否有数据**：

- exists()：判断查询集中是否有数据，如果有则返回True，没有则返回False。

#### 两大特性

##### 1）惰性执行

创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用

例如，当执行如下语句时，并未进行数据库查询，只是创建了一个查询集qs

```python
qs = Student.objects.all()
```

继续执行遍历迭代操作后，才真正的进行了数据库的查询

```python
for student in qs:
    print(student.name)
```



##### 2）缓存

使用同一个查询集，第一次使用时会发生数据库的查询，然后Django会把结果缓存下来，再次使用这个查询集时会使用缓存的数据，减少了数据库的查询次数。

**情况一**：如下是两个查询集，无法重用缓存，每次查询都会与数据库进行一次交互，增加了数据库的负载。

```python
from booktest.models import Student
[student.id for student in Student.objects.all()]
[student.id for student in Student.objects.all()]
```



**情况二**：经过存储后，可以重用查询集，第二次使用缓存中的数据。

```python
qs=Student.objects.all()
[student.id for student in qs]
[student.id for student in qs]
```



#### 限制查询集

可以对查询集进行取下标或切片操作，等同于sql中的limit和offset子句。

> 注意：不支持负数索引。

**对查询集进行切片后返回一个新的查询集，不会立即执行查询。**

如果获取一个对象，直接使用[0]，等同于[0:1].get()，但是如果没有数据，[0]引发IndexError异常，[0:1].get()如果没有数据引发DoesNotExist异常。

示例：获取第1、2项，运行查看。

```python
qs = Student.objects.all()[0:2]
```



