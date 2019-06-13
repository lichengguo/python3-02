def simple_middleware(get_response):
    print('__init__初始化')

    def middleware(request):
        print('视图执行请求之前的代码')
        response = get_response(request)
        print('视图执行后的代码')
        return response

    return middleware


def simple_middleware2(get_response):
    print('__init__2222初始化')

    def middleware(request):
        print('视图执行请求之前的代码22222')
        response = get_response(request)
        print('视图执行后的代码2222')
        return response

    return middleware
