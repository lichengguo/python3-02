import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "路飞学城"  # 设置站点标题
    site_footer = "路飞学城有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)


from .models import Student

class StudentModelAdmin(object):
	list_display = ['id', 'name', 'age', 'sex',"class_no"]
	search_fields = ['id', 'name']
	show_detail_fields=["name"]
	ordering=["id","age"]
	refresh_times=[2,3,5,10,15]
	model_icon = 'fa fa-gift'
	readonly_fields =["name"]

xadmin.site.register(Student,StudentModelAdmin)