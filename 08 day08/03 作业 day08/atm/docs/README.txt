作者:Alnk(李成果)
版本:v1.0

程序介绍：
    功能全部用python知识完成，用到了 os\sys\json\模块导入\面向对象编程 等知识
    用户角色：
        实现ATM常用功能，如查看账户信息、提现、还款、转账、支付等
    管理员角色：
        添加账户、调整用户额度、冻结/激活账户、查看用户信息等功能

程序启动方式:
    直接运行 atm/bin/start.py 文件

登录账号密码：
    管理员账号
        账号:admin
        密码:123
    普通用户
        账号:123456
        密码：123
        账号:123456
        密码：123
        账号:286137
        密码：123

程序结构(tree/f)：
    ├─bin               # 执行目录
    │  │  start.py          # 执行文件
    │
    ├─conf              # 配置文件目录
    │  │  settings.py       # 配置文件
    │
    ├─core              # 核心代码目录
    │  │  admin.py          # 管理员模块
    │  │  basic.py          # 基础模块
    │  │  decorator.py      # 装饰器模块，外部调用付款接口时会用到
    │  │  log.py            # 日志模块
    │  │  login.py          # 登录认证木块
    │  │  main.py           # 功能分发模块
    │  │  user.py           # 普通用户模块
    │
    ├─db                # 数据目录
    │  │
    │  └─user_info     # 用户登录信息目录
    │          123456.json  # 普通文件，可以用管理员账号创建
    │          215233.json
    │          286137.json
    │          admin.json   # 管理员初始化文件，记录账号密码权限等信息
    │
    ├─docs              # 文档目录
    │      README.txt       # 程序说明文件
    │      需求.txt         # 需求
    │
    ├─log               # 日志记录目录
    │      123456.log       #普通用户日志
    │      215233.log
    │      admin.log        # 管理员日志文件

db/user_info/admin.json 文件示例说明
    user_dict = {
        'name': name,  # 账号
        'pwd': pwd,  # 密码
        'role': role,  # 角色 管理员:admin, 用户:user
        'total_quota': total_quota,  # 总额度
        'available_quota': total_quota,  # 可用额度
        'state': 1,  # 状态 1：可用，0：冻结
    }
