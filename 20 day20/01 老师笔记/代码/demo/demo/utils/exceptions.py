from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
def custom_exception_handler(exc, context):
	"""
	:param exc         异常发生时的类对象
	:param context     异常发生时的执行上下文[可以通过它获取异常发生时的时间、文件、视图名称等。。。]
	"""

	# 先调用drf本身提供的异常处理函数
	response = exception_handler(exc,context)
	# response 的返回值，如果是None,则有以下2种可能：
	# 1. 程序本身没有任何问题
	# 2. drf的异常处理函数没有识别到
	if response is None:
		if isinstance(exc, ZeroDivisionError):
			print("0不能作为除数！")
			view = context['view']
			print('[%s]: %s' % (view, exc))
			response = Response("服务器内部错误", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	return response