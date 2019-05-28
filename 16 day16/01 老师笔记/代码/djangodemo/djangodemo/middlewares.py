def simple_middleware1(get_response):
	# 项目启动时执行的代码。
	print("simple_middleware1---__init__项目初始化")

	# 这个子函数会在用户请求的时候才会执行
	def middleware(request):
		# 此处编写的代码会在每个请求处理视图前被调用。
		print("simple_middleware1---视图执行请求之前的代码,解密,验证权限")
		response = get_response(request)

		# 此处编写的代码会在每个请求处理视图之后被调用。
		print("simple_middleware1---视图执行响应之后的代码,加密,操作记录")
		return response

	return middleware

def simple_middleware2(get_response):
	# 项目启动时执行的代码。
	print("simple_middleware2---__init__项目初始化")

	# 这个子函数会在用户请求的时候才会执行
	def middleware(request):
		# 此处编写的代码会在每个请求处理视图前被调用。
		print("simple_middleware2---视图执行请求之前的代码,解密,验证权限")
		response = get_response(request)

		# 此处编写的代码会在每个请求处理视图之后被调用。
		print("simple_middleware2---视图执行响应之后的代码,加密,操作记录")
		return response

	return middleware