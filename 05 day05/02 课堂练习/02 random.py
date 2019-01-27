import random


def random_code():
    """随机验证码"""
    code = ''
    for i in range(6):
        ret = str(random.randint(0, 9))
        alf = chr(random.randint(97, 122))
        res = random.choice([ret, alf])
        code += res
    print(code)


random_code()

