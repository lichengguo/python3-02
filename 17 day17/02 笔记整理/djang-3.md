## 1 模板引擎

今天的学习代码，我们保存在temp子应用下面，

```python
python manage.py startapp temp
```





### 1.1 模板使用

在项目中创建模板目录templates。

在settings.py配置文件中修改**TEMPLATES**配置项的DIRS值：

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')，  # 此处修改
        ],  
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
```



#### 1.1.1 定义模板

在templates目录中新建一个模板文件，如index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{ city }}</h1>
</body>
</html>
```



#### 1.1.2 模板渲染

调用模板分为两步骤：

1. 找到模板 loader.get_template(模板文件在模板目录中的相对路径) -> 返回模板对象
2. 渲染模板 模板对象.render(context=None, request=None) -> 返回渲染后的html文本字符串 context 为模板变量字典，默认值为None request 为请求对象，默认值为None

例如，定义一个视图

```python
from django.http import HttpResponse
from django.template import loader

def index(request):
    # 1.获取模板
    template=loader.get_template('index.html')

    context={'city': '北京'}
    # 2.渲染模板
    return HttpResponse(template.render(context))
```

**Django提供了一个函数render可以简写上述代码。**

render(request对象, 模板文件路径, 模板数据字典)

```python
from django.shortcuts import render

def index(request):
    # context = {'city': '北京'}
    # return render(request, 'index.html', context)
    return render(request, 'index.html', {'city': '北京1'})  # 也可以这样写
```



#### 1.1.3 模板语法



##### 1.1.3.1 模板变量

变量名必须由字母、数字、下划线（不能以下划线开头）和点组成。

语法如下：

```python
{{ 变量 }}
```

模板变量可以使python的内建类型，也可以是对象。

```python
# 视图文件中
from django.views import View
class HomeView(View):
    def get(self, request):

        return render(request, 'index.html', {
            "title": '新的标题',
            'tuple': (1, 2, 3, 4,),
            'list1': ['a', 'b', 'c', ],
            'dict1': {'name': 'alnk', 'age': 18, }
        })

 
# html模版文件中
!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>输出元组成员，必须使用 点 语法</p>
    <p>{{ tuple }}</p>
    <p>{{ tuple.0 }}</p>
    <p>{{ tuple.1 }}</p>
    <p>输出列表成员，必须使用 点 语法</p>
    <p>{{ list1 }}</p>
    <p>{{ list1.1 }}</p>
    <p>{{ list1.0 }}</p>
    <p>输出字典成员，必须使用 点 语法</p>
    <p>{{ dict1 }}</p>
    <p>{{ dict1.name }}</p>
    <p>{{ dict1.age }}</p>
    <p>不可以直接调用函数</p>
    <p>不支持模板中编写表达式</p>
</body>
</html>
```



##### 1.1.3.2 模板语句

**for循环：**

```python
{% for item in 列表 %}

循环逻辑
{{for loop.counter}}表示当前是第几次循环，从1开始

{%empty%} 列表为空或不存在时执行此逻辑

{% endfor %}
```

例子1：

视图文件

```python
from django.views import View


class HomeView(View):

    def get(self, request):

        return render(request, 'index2.html', {
            'tuple': (1, 2, 3, 4,),
            'list1': ['a', 'b', 'c', ],
            'dict1': {'name': 'alnk', 'age': 18, },
        })
```

模版文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h3>循环语句可以提取每一个复合类型数据的成员</h3>
    <p>列表</p>
    {% for i in list1 %}
        <li>{{ i }}</li>
    {% endfor %}

    <p>元组</p>
    {% for foo in tuple %}
        <li>{{ foo }}</li>
    {% endfor %}


    <p>字典</p>
    {% for i,k in dict1.items %}
        <li>{{ i }} - {{ k }}</li>
    {% endfor %}
    
    <p>输出下标</p>
    {% for foo in list1 %}
        <li>序号{{ forloop.counter0 }} - {{ foo }}</li>
    {% endfor %}
    
    
</body>
</html>
```

例子2

视图文件

```python
from django.views import View


class HomeView(View):
    def get(self, request):

        return render(request, 'index3.html', {
            'book_list': [
                {'name': 'python', 'price': 99},
                {'name': 'go', 'price': 69},
            ]
        })
```

```html
# 模版文件
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<table border="1">
    <thead>
        <tr>
            <th>序号[从0开始]</th>
            <th>序号[从1开始]</th>
            <th>序号[反转]</th>
            <th>名词</th>
            <th>价格</th>
        </tr>
    </thead>
    <tbody>
        {% for book in book_list %}
            <tr>
                <td>{{ forloop.counter0 }}</td>
                <td>{{ forloop.counter }}</td>
                <td>{{ forloop.revcounter }}</td>
                <td>{{ book.name }}</td>
                <td>{{ book.price }}</td>
            </tr>
        {% endfor %}

    </tbody>
</table>


</body>
</html>
```



**if条件：**

```python
{% if ... %}
逻辑1
{% elif ... %}
逻辑2
{% else %}
逻辑3
{% endif %}
```

比较运算符如下：

```
==
!=
<
>
<=
>=
```

布尔运算符如下：

```
and
or
not
```

**注意：运算符左右两侧不能紧挨变量或常量，必须有空格。**

```python
{% if a == 1 %}  # 正确
{% if a==1 %}  # 错误
```

例子1

views.py 视图文件

```python
from django.views import View

class HomeView(View):  

    def get(self, request):
        return render(request, 'index3.html', {
            'book_list': [
                {'name': 'python', 'price': 99},
                {'name': 'go', 'price': 69},
                {'name': 'go', 'price': 69},
                {'name': 'go', 'price': 69},
                {'name': 'go', 'price': 69},
            ]
        })

```

模板文件 .html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>循环语句和判断语句可以嵌套使用</h3>

<table border="1">
    <thead>
        <tr>
            <th>序号[从0开始]</th>
            <th>序号[从1开始]</th>
            <th>序号[反转]</th>
            <th>名词</th>
            <th>价格</th>
        </tr>
    </thead>
    <tbody>
        {% for book in book_list %}
            {% if forloop.first %}
                <tr style="background: orange">
            {% elif forloop.last %}
                <tr style="background: blue">
            {% else %}
                <tr></tr>
            {% endif %}
                    <td>{{ forloop.counter0 }}</td>
                    <td>{{ forloop.counter }}</td>
                    <td>{{ forloop.revcounter }}</td>
                    <td>{{ book.name }}</td>
                    <td>{{ book.price }}</td>
                </tr>
        {% endfor %}

    </tbody>
</table>


</body>
</html>
```



例子2

视图文件

```python
class HomeView(View):

    def get(self, request):
        # forloop.parentloop.counter 会继承上一个for循环的计数规则
        return render(request, 'index4.html', {
            'people': [
                {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
                {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
                {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
                {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
                {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
            ]
        })
```

模板html文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>循环语句和判断语句可以嵌套使用</h3>

<table border="1">
    <thead>
        <tr>
            <th>序号</th>
            <th>姓名</th>
            <th>年龄</th>
            <th>爱好</th>
        </tr>
    </thead>
    <tbody>
        {% for book in people %}
            <tr>
                <td>{{ forloop.counter }}</td>
                <td>{{ book.name }}</td>
                <td>{{ book.age }}</td>
                <td>
                    {% for lv in book.love %}
                        第{{ forloop.parentloop.counter }}人的第{{ forloop.counter }}爱好：{{ lv }} <br>
                    {% endfor %}
                </td>
            </tr>
       {% empty %}   # 针对没有数据的情况
            <tr>
                <td colspan="4">没有数据</td>
            </tr>
        {% endfor %}

    </tbody>
</table>


</body>
</html>
```



##### 1.1.3.3 过滤器

语法如下:

- 使用管 道符号| 来应用过滤器，用于进行计算、转换操作，可以使用在变量、标签中。

- 如果过滤器需要参数，则使用冒号:传递参数。

  ```python
  变量|过滤器:参数
  ```

列举几个如下：

- **safe**，禁用转义，告诉模板这个变量是安全的，可以解释执行

- **length**，长度，返回字符串包含字符的个数，或列表、元组、字典的元素个数。

- **default**，默认值，如果变量不存在时则返回默认值。

  ```
  data|default:'默认值'
  ```

- **truncatewords** 文本截取

- **date**，日期，用于对日期类型的值进行字符串格式化，常用的格式化字符如下：

  - Y表示年，格式为4位，y表示两位的年。
  - m表示月，格式为01,02,12等。
  - d表示日, 格式为01,02等。
  - j表示日，格式为1,2等。
  - H表示时，24进制，h表示12进制的时。
  - i表示分，为0-59。
  - s表示秒，为0-59。

  ```
  value|date:"Y年m月j日  H时i分s秒"
  ```

例子

视图文件

```python
from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        """过滤器"""
        from datetime import datetime
        return render(request, "index5.html", {
            "title": "welcome to django",
            'title2': '<h1>大标题</h1>',
            'title3': "小可爱",
            'date_time': datetime.now(),
            'str1': 'welcome to django',
            'str2': '我爱中国 welcome to django'
        })
```

模板html文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h3>过滤器</h3>
    <p>使用普通方法，如果没有参数，可以直接使用，不用加小括号</p>
    <p>{{ title | upper }}</p>
    <p>{{ title }}</p>

    <hr>
    <p>默认情况下，django输出内容的时候，会判断是否有html标签，有则会进行转转义
    为什么要转义呢？为了网站安全，不会被别人在留言或者表单中xss攻击（跨站脚本攻击）</p>
    <p>我们有时候也会在页面输出我们信任的html内容，可以使用safe过滤器</p>
    {{ title2 | safe }}

    <hr>
    {{ title3 | default:"默认值" }}

    <hr>
    {{ date_time | date:"Y年m月j日" }}

    <hr>
    <p>按字符截取长度</p>
    <p>{{ str1 | truncatechars:3  }}</p>

    <p>按单词截取长度，对于中文词语不识别</p>
    <p>{{ str2 | truncatewords:2 }}</p>

</body>
</html>
```



##### 1.1.3.4 注释

单行注释语法如下：

```
{#...#}
```

多行注释使用comment标签，语法如下：

```python
{% comment %}
...
{% endcomment %}
```



### 1.2 模版分离

模板分离可能造成项目中出现很多碎片化的模板，这样的分离方式，会导致以后维护一个网站的页面，涉及到很多的小模板，不好管理维护，因此出现了模板继承

![](素材\1.png)

例子：

被引入的html文件

```html
<p>head公共的头部代码</p>
```

模板文件1

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>首页页面</h1>
    {% include "index/head_pub.html" %}
    <p>首页独有的代码</p>
    <p>公共的底部代码</p>
</body>
</html>
```

模板文件2

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>列表页</h1>
    {% include "index/head_pub.html" %}
    <p>列表页独有的代码</p>
    <p>公共的底部代码</p>
</body>
</html>
```





### 1.3 模板继承

模板分离可能造成项目中出现很多碎片化的模板，这样的分离方式，会导致以后维护一个网站的页面，涉及到很多的小模板，不好管理维护，因此出现了模板继承



学习模板继承之前，我们需要先了解2个概念！

**面向对象的继承**

```
不同的子类可以把公共的方法或属性，抽象到父类中。
父类拥有的属性或方法，子类都可以通过继承到
子类还可以重写父类的同名方法或者同名属性的值
```



**模板共用**

```
在开发网站时，一个网站会很多页面，不用页面之间，肯定会存在部分一样的页面部分，例如：
头部、脚部、菜单、广告窗。。。
```



模板继承和类的继承含义是一样的，主要是为了提高代码重用，减轻开发人员的工作量。

**父模板**

如果发现在多个模板中某些内容相同，那就应该把这段内容定义到父模板中。

标签block：用于在父模板中预留区域，留给子模板填充差异性的内容，名字不能相同。 为了更好的可读性，建议给endblock标签写上名字，这个名字与对应的block名字相同。父模板中也可以使用上下文中传递过来的数据。

```python
{% block 名称 %}
预留区域，可以编写默认内容，也可以没有默认内容
{% endblock  名称 %}
```

**子模板**

标签extends：继承，写在子模板文件的第一行。

```
{% extends "父模板路径"%}
```

子模版不用填充父模版中的所有预留区域，如果子模版没有填充，则使用父模版定义的默认值。

填充父模板中指定名称的预留区域。

```
{% block 名称 %}
实际填充内容
{{ block.super }}用于获取父模板中block的内容
{% endblock 名称 %}
```



![](素材\2.png)

例子

base.html 父模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    <p>公共头部</p>

    {% block content %}
    公共中间内容
    {% endblock content %}

    <p>公共底部</p>

</body>
</html>
```

index.html 子模板 继承父模板

```html
{% extends 'exten/base.html' %}

{% block content %}

    首页里大段大段的代码<br>
    继承父模板的代码： {{ block.super }}
{% endblock content %}
```

list.html 子模板 继承父模板

```html
{% extends 'exten/base.html' %}
```



 

## 2 表单系统

是django.forms提供的,可以简化并自动化大部分的表单处理工作。

使用django提供的表单系统可以快速生成表单的html，以及默认django提供的表单系统内置了表单验证提示等相关的表单功能。



步骤:

1. 声明表单类，表单类必须要继承于 django.forms.Form类 或继承于 django.forms.ModelForm
2. 把表单类导入到视图,并对表单类进行实例化
3. 通过视图，把表单类实例对象传递模板中。
4. 在模板中显示
5. 在视图中还可以表单信息并校验表单信息



### 2.1 声明表单类

表单系统的核心部分是Django的 Form 类。 Django 的数据库模型描述一个对象的逻辑结构、行为以及展现给我们的方式，与此类似，Form类描述一个表单并决定它如何工作和展现。

假如我们想在网页中创建一个表单，用来获取用户想保存的图书信息，可能类似的html 表单如下：

```html
<form action="" method="post">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit">
</form>
```



我们可以据此来创建一个Form类来描述这个表单。

在子应用中新建一个**forms.py**文件，编写Form类。

```python
from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(max_length=6, required=True, help_text="账号不能为空，并且长度必须在6-16个字符之间", label="账号")
	password = forms.CharField(required=True, help_text="密码不能为空，并且长度必须在6-16个字符之间", label="密码")
```

注：[表单字段类型参考资料连接](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/fields/)



### 2.2 视图中使用表单类

```python
from django.shortcuts import render
from .forms import LoginForm
class UserView(View):
	def get(self,request):

		return render(request,"form.html",{
			"forms":LoginForm(),  # 把表单类导入到视图,并对表单类进行实例化
		})
```



### 2.3 模板中使用表单类

可以选择自己手动美化表单，也可以引入bootstrap的样式外观。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户登陆</title>
    <style>
    .helptext{
        background: #ddd;
        padding: 2px 20px;
        border-radius: 3px;
        display: block;
        margin: 10px 0;
    }
    form label{
        display: block;
    }
    </style>
</head>
<body>
    <form action="" method="post">
        {% csrf_token %}
        {{ forms }}
        <input type="submit" value="登陆">
    </form>
</body>
</html>
```

- csrf_token 用于添加CSRF防护的字段
- forms 快速渲染表单字段的方法



### 2.4 验证用户提交的表单数据

```python
from .forms import LoginForm
class UserView(View):
	def get(self,request):
		....
    
	def post(self,request):
		"""提交表单"""
		# 使用表单系统提供的验证流程
		form = LoginForm(request.POST)  # 必须实例化表单类
		if form.is_valid(): # is_valid 验证函数,会提取表单中的限制选项进行进行验证
			print( form.cleaned_data )
			print( "到数据库中查询账号密码,进行数据对比" )
            return HttpResponse("ok")
		else:
			print("验证失败!")
            # 这里是表单验证错误信息显示
            return render(request,"form.html",{
                # 这里必须返回的是用户提交过的表单对象，这个表单对象里面才会有错误信息
                "forms":form,
            })
```

- form.is_valid() 验证表单数据的合法性
- form.cleaned_data 验证通过的表单数据



如果要在浏览器显示报错信息，那么模板文件需要引入报错信息

当然，也可以不引用，也会有提示

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录页面</title>
    <style>
        .helptext {
            display: block;
        }
    </style>
</head>
<body>

<form action="" method="post">
{#    账号：<input type="text" name="user"><br><br>#}
{#    密码：<input type="password" name="pwd"><br><br>#}
    
    {# 报错信息 #}
    {% for foo in forms.username.errors %}
        {{ foo }}
    {% endfor %}
    
    {#csrf跨站伪造保护#}
    {% csrf_token %}
    
    {#调用视图传过来的变量，表单#}
    {{ forms }}
    
    <input type="submit" value="登录">
</form>

</body>
</html>
```



除了声明表单类的字段选项以外，django还提供了2个方式供我们开发者进行表单数据的验证，一般使用的时候二选一。

validators自定义函数验证

```python
from django import forms
from django.core.exceptions import ValidationError

# 自定义验证函数
def checkusername(data):
	if data == "None":
		# 抛出异常
		raise ValidationError("用户名不能是None!")
	# 验证函数里面如果通过了验证，必须返回数据!
	return data

class LoginForm(forms.Form):
  # validators的值可以是多个，也就说可以对一个字段进行多次的验证。
	username = forms.CharField(validators=[checkusername], max_length=6, required=True, help_text="账号不能为空，并且长度必须在6-16个字符之间", label="账号")
	password = forms.CharField(required=True, help_text="密码不能为空，并且长度必须在6-16个字符之间", label="密码")
```



clean自定义方法进行验证

```python
class LoginForm(forms.Form):
	username = forms.CharField(max_length=6, required=True, help_text="账号不能为空，并且长度必须在6-16个字符之间", label="账号")
	password = forms.CharField(required=True, help_text="密码不能为空，并且长度必须在6-16个字符之间", label="密码")
	remember = forms.BooleanField(required=False,label="是否记住密码")

	# 验证单个字段 方法的命名规范必须是 clean_<字段名>(self):
	def clean_username(self):
		"""自定义验证表单字段的方法"""
		# cleaned_data 字典类型，用户提交过来的数据
		data = self.cleaned_data.get("username")
		if data == "老男孩":
			raise ValidationError("用户名不能是老男孩！")
		else:
			# 验证函数里面如果通过了验证，必须返回数据!
			return data

	# 验证所有字段，方法名必须是 clean(self)
	def clean(self):
		password = self.cleaned_data.get("password")
		if not password:
			raise ValidationError("登录密码不能为空！")
		return self.cleaned_data
```

不管是 validators 或者 clean 或者字段选项里面验证，都是在视图中调用 form.is_valid() 时才进行的验证。



### 2.5 模型类表单

如果表单中的数据与模型类对应，可以通过继承**forms.ModelForm**更快速的创建表单。

forms.py 表单文件

```python
"""From 基本表单类
	    所有的字段和验证选项，都需要我们手动声明
	    
   ModelForm 模型表单类
		可以支持我们声明表单中的字段，从指定的模型中进行生成
"""
from users.models import Student  # 从user子项目中导入models中的student数据库模型类
class UserForm(forms.ModelForm):
	class Meta:
		model = Student
		# fields = "__all__"  # 这里表示从模型中继承所有的字段过来,作为表单项显示到页面那种
		# fields = ["name","sex","class_no"] # 这里表示从模型中继承列表中指定的字段作为表单项
		exclude = ["is_delete"]   # 这里表示从模型中继承除了列表中以外的字段作为表单项,这个选项和fields相反
```

- model 指明从属于哪个模型类
- fields 指明向表单中添加模型类的哪个字段

视图文件 views.py

```python
from .forms import UserForm


class FormModelView(View):
    def get(self, request):
        return render(request, 'form_model.html', {
            'form_content': UserForm(),
        })

```



模板文件文件

form_mode.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录页面</title>
    <style>
        .helptext {
            display: block;
        }
        form label {
            display: block;
        }
    </style>
</head>
<body>

<form action="" method="post">
    {% csrf_token %}
    {{ form_content }}
    <input type="submit" value="登录">
</form>

</body>
</html>
```

**模型类表单与普通表单的验证方式和自定义验证都是一致的**.





## 3 案例: 学生信息录入系统

创建一个子应用stusys

```
python manage.py startapp stusys
```

创建路由文件以及在总路由中注册当前子路由文件

stusys/urls.py,代码;

```python
from django.urls import path,re_path
urlpatterns = [

]
```



主应用/urls.py

```python
urlpatterns = [
		....
    path("sys/", include("stusys.urls") ),
]
```

接下来，在settings.py文件注册子应用

```python
# 子应用注册列表
INSTALLED_APPS = [
	  ....
    'stusys',
]
```



创建视图类，先设置针对数据的增删查改方法

```python
from django.shortcuts import render
from django.views import View
# Create your views here.
"""
针对一个功能的实现，基本要完成5个方法：
1. 获取所有数据  students/
3. 添加一条数据  students/

2. 获取一条数据  students/10/
4. 修改一条数据  students/10/
5. 删除一条数据  students/10/
"""
class StudentListView(View):
	def get(self,request):
		"""获取所有数据"""
		pass

	def post(self,request):
		"""添加一条数据"""
		pass
	
class StudentView(View):
	def get(self,request):
		"""获取一条数据"""
		pass
	
	def put(self,request):
		"""修改一条数据"""
		pass
	
	def delete(self,request):
		pass
```

绑定路由

```python
from django.urls import path,re_path
from . import views
urlpatterns = [
	path("students/", views.StudentListView.as_view()),
	re_path("students/(?P<pk>\d+)/", views.StudentView.as_view()),
]
```



完成学生信息的列表页

在templates创建sys目录，并提供了列表页模板list.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    h1{
        font-size: 22px;
        font-weight: normal;
        text-align: center;
        border-bottom: 1px solid #aaa;
        padding-bottom: 20px;
    }
    .btn{
        background-color: dodgerblue;
        border-radius: 3px;
        text-align: center;
        color: #fff;
        padding: 4px 12px;
        text-decoration: none;
        display: inline-block;
        margin: 10px 0px;
    }
    .table{
        border-collapse: collapse;
        border: 1px solid #ddd;
        width: 600px;
    }
    .table td,.table th{
        height: 25px;
        font-size: 14px;
        font-weight: normal;
        border: 1px solid #ddd;
    }
    .table th{
        background-color: aliceblueu;
    }
    </style>
</head>
<body>
    <h1>学生信息录入系统</h1>
    <a class="btn" href="">添加学生信息</a>
    <table class="table">
        <tr>
            <th>ID</th>
            <th>姓名</th>
            <th>年龄</th>
            <th>性别</th>
            <th>班级</th>
            <th>操作</th>
        </tr>
        <tr>
            <td>姓名</td>
            <td>姓名</td>
            <td>姓名</td>
            <td>姓名</td>
            <td>姓名</td>
            <td>
                <a class="btn" href="">更新</a>
                <a class="btn" href="">删除</a>
            </td>
        </tr>
    </table>
</body>
</html>
```



在视图中展示列表页面

```python
from users.models import Student  # 导入数据库模型
class StudentListView(View):
	def get(self,request):
		"""获取所有数据"""
		# 1. 获取数据库里面的所有学生信息
		student_list = Student.objects.filter(is_delete=False).all()
		# 2. 渲染模板
		return render(request,"sys/list.html",{
			"students_list":student_list,
		})
```

列表页模板代码:

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    h1{
        font-size: 22px;
        font-weight: normal;
        text-align: center;
        border-bottom: 1px solid #aaa;
        padding-bottom: 20px;
    }
    .btn{
        background-color: dodgerblue;
        border-radius: 3px;
        text-align: center;
        color: #fff;
        padding: 4px 12px;
        text-decoration: none;
        display: inline-block;
        margin: 10px 0px;
    }
    .table{
        border-collapse: collapse;
        border: 1px solid #ddd;
        width: 600px;
    }
    .table td,.table th{
        text-align: center;
        height: 25px;
        font-size: 14px;
        font-weight: normal;
        border: 1px solid #ddd;
    }
    .table th,.th{
        text-align: center;
        background-color: aliceblueu;
    }
    </style>
</head>
<body>
    <h1>学生信息录入系统</h1>
    <a class="btn" href="">添加学生信息</a>
    <table class="table">
        <tr>
            <th>ID</th>
            <th>姓名</th>
            <th>年龄</th>
            <th>性别</th>
            <th>班级</th>
            <th>操作</th>
        </tr>
        {% for student in students_list %}
        <tr>
            <td>{{ student.id }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.age }}</td>
            <td>{{ student.sex_text }}</td>
            <td>{{ student.class_no }}</td>
            <td>
                <a class="btn" href="">更新</a>
                <a class="btn" href="">删除</a>
            </td>
        </tr>
        {% empty %}
        <tr>
            <td class="th" colspan="6">暂无信息！</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```



编辑学生信息

我们协定了更新页面的url地址,是`/sys/students/<id>/`,所以注册路由信息

```python
from django.urls import path,re_path
from . import views
urlpatterns = [
	# path("students/", views.StudentListView.as_view()),
	# re_path("students/(?P<pk>\d+)/", views.StudentView.as_view()),
	re_path("students/update/(?P<pk>\d+)/", views.StudentUpdateView.as_view()),
]
```

在templates/sys/目录下创建update.html模板,代码:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>更新学生信息</title>
</head>
<body>
    <form action="">
        {%  csrf_token %}
        <input type="submit" value="更新">
    </form>
</body>
</html>
```



视图中,接受ID,并加载模板

```python
class StudentUpdateView(View):
	def get(self,request,pk):
		"""获取要更新的数据"""

		print(pk)

		return render(request,"sys/update.html")
```



根据ID获取学生信息,并展示到模板中.

stusys/forms.py,声明表单类

```python
from django import forms
from users.models import Student
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ("is_delete", )
```

视图中根据ID获取数据,并调用表单类进行实例化,传值给客户端

```python
from users.models import Student
from .forms import StudentForm
class StudentUpdateView(View):
	def get(self,request,pk):
		"""获取要更新的数据"""

		# 根据ID获取学生信息
		try:
			student = Student.objects.get(pk=pk)
		except Student.DoesNotExist:
			return redirect("对不起,参数有误!")

		data = {}
		data["name"] = student.name
		data["sex"] = student.sex
		data["age"] = student.age
		data["class_no"] = student.class_no
		data["born"] = student.born
		data["money"] = student.money
		data["description"] = student.description

		# 把表单类显示到模板中
		return render(request,"sys/update.html",{
			"forms": StudentForm(data)
		})
```



更新页面的模板显示表单信息

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>更新学生信息</title>
    <style>
    label{
        display: block;
    }
    </style>
</head>
<body>
    <form action="" method="post">
        {%  csrf_token %}
        {{ forms }}
        <input type="submit" value="更新">
    </form>
</body>
</html>
```



接收表单提交的数据并验证表单数据

```python
from users.models import Student
from .forms import StudentForm
class StudentUpdateView(View):
	def get(self,request,pk):
		"""获取要更新的数据"""

		# 根据ID获取学生信息
		try:
			student = Student.objects.get(pk=pk)
		except Student.DoesNotExist:
			return redirect("对不起,参数有误!")

		data = {}
		data["name"] = student.name
		data["sex"] = student.sex
		data["age"] = student.age
		data["class_no"] = student.class_no
		data["born"] = student.born
		data["money"] = student.money
		data["description"] = student.description

		# 把表单类显示到模板中
		return render(request,"sys/update.html",{
			"forms": StudentForm(data)
		})

	def post(self,request,pk):
		"""更新数据"""
		# 调用表单类进行验证
		form = StudentForm(request.POST)

		if form.is_valid():
			# 验证通过
			data = form.cleaned_data
			# 数据库操作
			try:
				student = Student.objects.get(pk=pk)
				student.name = data.get("name")
				student.class_no = data.get("class_no")
				student.sex = data.get("sex")
				student.age = data.get("age")
				student.money = data.get("money")
				student.born = data.get("born")
				student.description = data.get("description")
				student.save()
				return redirect("/sys/students/")
			except Student.DoesNotExist:
				return render(request, "sys/update.html", {
					"forms": form,
				})
		else:
			# 验证失败
			return render(request,"sys/update.html",{
				"forms":form,
			})
```

